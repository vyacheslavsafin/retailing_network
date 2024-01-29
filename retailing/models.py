from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Dealer(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    email = models.EmailField(max_length=100, verbose_name='email')
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица')
    house = models.CharField(max_length=50, verbose_name='дом')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата выхода продукта на рынок')
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, verbose_name='Поставщик')

    def __str__(self):
        return f'{self.title} ({self.dealer})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
