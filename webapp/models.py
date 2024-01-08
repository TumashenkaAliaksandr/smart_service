from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)  # Поле для названия брэнда
    photo = models.ImageField(upload_to='brand_photos/')  # Поле для фото брэнда, сохраняемое в папке 'brand_photos/'

    def __str__(self):
        return self.name  # Возвращает название брэнда в админке Django
