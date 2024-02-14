from django.contrib import admin
from .models import *


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_preview')  # Отображаемые поля в списке брэндов

    def photo_preview(self, obj):
        return obj.photo.url if obj.photo else None  # Отображение превью изображения в админке

    photo_preview.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'description_two', 'image', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Shop_Encoders)
class Shop_EncodersAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'description_two', 'image', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Shop_Board)
class Shop_BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'description_two', 'image', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Favors)
class FavorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'description_two', 'image', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения