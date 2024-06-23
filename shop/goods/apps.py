from django.apps import AppConfig


class GoodsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'goods'
    # Меняем имя приложения в админ панели Django
    verbose_name = 'Товары'
