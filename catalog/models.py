import datetime

from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name='наименование')
    about = models.TextField(blank=True, verbose_name='описание')
    image = models.ImageField(upload_to='products/', verbose_name='превью')
    category = models.CharField(max_length=300, verbose_name='категория')
    price_lot = models.IntegerField(verbose_name='цена за покупку')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    date_last_change = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}: {self.about}'

    class Meta:
        verbose_name = 'Продукция'
        database = 'Product'


class Category(models.Model):
    name = models.CharField(max_length=300, verbose_name='наименование')
    about = models.TextField(blank=True, verbose_name='описание')

    def __str__(self):
        return f'{self.name}: {self.about}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        database = 'default'

