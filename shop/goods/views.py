from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, get_list_or_404, render
from goods.models import Products


def catalog(request, category_slug='all'):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    else:
        # 404 если ничего нет (первый способ)
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        # Отрисовака страницы если ничего нету (второй способ)
        # if not goods.exists():
        #     render()

    if on_sale:
        goods = goods.filter(discount__gt=0)
    if order_by:
        goods = goods.filter(order_by)
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - Каталог',
        'goods': current_page,
    }

    return render(request, 'goods/catalog.html', context)


def product(request, product_slug=False, product_id=False):
    # Проверяем к чему запрос? к id или slug и выводим результат
    if product_id:
        product = Products.objects.get(id=product_id)
    if product_slug:
        product = Products.objects.get(slug=product_slug)
    
    context = {
        'product':product
    }

    return render(request, 'goods/product.html', context)
