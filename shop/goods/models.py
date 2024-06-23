from django.db import models


class Categories(models.Model):
    # id поле создается автоматически
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        # Меняем имя таблицы
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name


class Products(models.Model):
    # P.s CharField - короткие строки, TextField - длинные строки
    name = models.CharField(max_length=150, unique=True, blank=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', null=True, verbose_name='Изображение')
    # max_digits=... кол-во цифр до запятой, decimal_places=... кол-во цифр после запятой
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    # PROTECT - запрещает удалять категорию и это хорошо
    # CASCADE - удаляется катагория и все товары в ней (будет предупреждение)
    # SET_DEFAULT - при удалении категории всем ее товарам будет присовено значение по умолчанию
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id', )


    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'
    
    def display_id(self):
        return f"{self.id:05}"  # Добавить нули чтобы сумарное значение было 5 символов
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price
