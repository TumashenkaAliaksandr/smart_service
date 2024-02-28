from django.db import models
from ckeditor.fields import RichTextField



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


class ServicesMain(models.Model):
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
        verbose_name = "Services MAIN"
        verbose_name_plural = "Services MAIN"

class Shop_Encoders(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    name_two = models.CharField(max_length=100, verbose_name='name_two', default='Второй Заголовок')
    description = RichTextField()
    description_two = RichTextField()
    description_three = RichTextField(verbose_name='description three', default='Описание')
    client_visit = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='services', verbose_name='photo')
    image_two = models.ImageField(upload_to='services', verbose_name='photo_two', default='default_image.jpg')
    image_three = models.ImageField(upload_to='services', verbose_name='photo_three', default='default_image_three.jpg')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Encoders"
        verbose_name_plural = "Encoders"


class Shop_Board(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    name_two = models.CharField(max_length=100, verbose_name='name_two', default='Второй Заголовок')
    description = RichTextField()
    description_two = RichTextField()
    description_three = RichTextField(verbose_name='description three', default='Описание')
    client_visit = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='services', verbose_name='photo')
    image_two = models.ImageField(upload_to='services', verbose_name='photo_two', default='default_image.jpg')
    image_three = models.ImageField(upload_to='services', verbose_name='photo_three', default='default_image_three.jpg')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Board"
        verbose_name_plural = "Board"


class Shop_Inverter(models.Model):
    """Inverter model"""
    name = models.CharField(max_length=100, verbose_name='name')
    name_two = models.CharField(max_length=100, verbose_name='name_two', default='Второй Заголовок')
    description = RichTextField()
    description_two = RichTextField()
    description_three = RichTextField()
    client_visit = RichTextField()
    image = models.ImageField(upload_to='services', verbose_name='photo')
    image_two = models.ImageField(upload_to='services', verbose_name='photo_two', default='default_image.jpg')
    image_three = models.ImageField(upload_to='services', verbose_name='photo_three', default='default_image_three.jpg')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Inverter"
        verbose_name_plural = "Inverter"


class Shop_Indastrial_Electroniks(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    name_two = models.CharField(max_length=100, verbose_name='name_two', default='Второй Заголовок')
    description = RichTextField()
    description_two = RichTextField()
    description_three = RichTextField(verbose_name='description three', default='Описание')
    client_visit = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='services', verbose_name='photo')
    image_two = models.ImageField(upload_to='services', verbose_name='photo_two', default='default_image.jpg')
    image_three = models.ImageField(upload_to='services', verbose_name='photo_three', default='default_image_three.jpg')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Indastrial-Electroniks"
        verbose_name_plural = "Indastrial-Electroniks"


class Shop_Bcm(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    name_two = models.CharField(max_length=100, verbose_name='name_two', default='Второй Заголовок')
    description = RichTextField()
    description_two = RichTextField()
    description_three = RichTextField(verbose_name='description three', default='Описание')
    client_visit = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='services', verbose_name='photo')
    image_two = models.ImageField(upload_to='services', verbose_name='photo_two', default='default_image.jpg')
    image_three = models.ImageField(upload_to='services', verbose_name='photo_three', default='default_image_three.jpg')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bloks BCM ECU SBC ECU TCU"
        verbose_name_plural = "Bloks BCM ECU SBC ECU TCU"


class Shop_Electro_Transport(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    name_two = models.CharField(max_length=100, verbose_name='name_two', default='Второй Заголовок')
    description = RichTextField()
    description_two = RichTextField()
    description_three = RichTextField(verbose_name='description three', default='Описание')
    client_visit = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='services', verbose_name='photo')
    image_two = models.ImageField(upload_to='services', verbose_name='photo_two', default='default_image.jpg')
    image_three = models.ImageField(upload_to='services', verbose_name='photo_three', default='default_image_three.jpg')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Electro Transport"
        verbose_name_plural = "Electro Transport"


class Shop_Repair_Operator(models.Model):
    """Services model"""
    name = models.CharField(max_length=100, verbose_name='name')
    name_two = models.CharField(max_length=100, verbose_name='name_two', default='Второй Заголовок')
    description = RichTextField()
    description_two = RichTextField()
    description_three = RichTextField(verbose_name='description three', default='Описание')
    client_visit = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='services', verbose_name='photo')
    image_two = models.ImageField(upload_to='services', verbose_name='photo_two', default='default_image.jpg')
    image_three = models.ImageField(upload_to='services', verbose_name='photo_three', default='default_image_three.jpg')
    is_main = models.BooleanField(default=False)
    link = models.URLField()  # Поле для хранения ссылки
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price', default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Repair of operator panels"
        verbose_name_plural = "Repair of operator panels"


class Brand(models.Model):
    name = models.CharField(max_length=100)  # Поле для названия брэнда
    photo = models.ImageField(upload_to='brand_photos/')  # Поле для фото брэнда, сохраняемое в папке 'brand_photos/'

    def __str__(self):
        return self.name  # Возвращает название брэнда в админке Django


class Callback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    message = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Process(models.Model):
    name = models.CharField(max_length=100)  # Поле для названия брэнда
    photo = models.ImageField(upload_to='process_photos/')  # Поле для фото брэнда, сохраняемое в папке 'procces_photos/'
    description = RichTextField(verbose_name='description', default='Описание')
    steps = models.IntegerField(verbose_name='Steps', default=0)

    def __str__(self):
        return self.name  # Возвращает название процесса в админке Django

    class Meta:
        verbose_name = "Our Process"
        verbose_name_plural = "Our Process"