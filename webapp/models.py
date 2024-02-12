from django.db import models



class Favors(models.Model):
    """Favors"""
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')
    description_two = models.TextField(verbose_name='description_two', default='Описание')
    image = models.ImageField(upload_to='services', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Favors"
        verbose_name_plural = "Favors"


class Services(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')
    description_two = models.TextField(verbose_name='description_two', default='Описание')
    image = models.ImageField(upload_to='services', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"

class Shop_Encoders(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    description = models.TextField(verbose_name='description')
    description_two = models.TextField(verbose_name='description_two', default='Описание')
    image = models.ImageField(upload_to='services', verbose_name='photo')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Encoders"
        verbose_name_plural = "Encoders"


class Brand(models.Model):
    name = models.CharField(max_length=100)  # Поле для названия брэнда
    photo = models.ImageField(upload_to='brand_photos/')  # Поле для фото брэнда, сохраняемое в папке 'brand_photos/'

    def __str__(self):
        return self.name  # Возвращает название брэнда в админке Django
