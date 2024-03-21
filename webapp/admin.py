from django.contrib import admin
from .models import *
from ckeditor.widgets import CKEditorWidget

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_preview')  # Отображаемые поля в списке брэндов

    def photo_preview(self, obj):
        return obj.photo.url if obj.photo else None  # Отображение превью изображения в админке

    photo_preview.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_preview', 'description', 'steps')  # Отображаемые поля в списке брэндов

    def photo_preview(self, obj):
        return obj.photo.url if obj.photo else None  # Отображение превью изображения в админке

    photo_preview.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(ServicesMain)
class ServicesMainAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'description_two', 'image', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Shop_Encoders)
class Shop_EncodersAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_two', 'description', 'description_two', 'description_three', 'client_visit', 'image', 'image_two', 'image_three', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Shop_Indastrial_Electroniks)
class Shop_Indastrial_ElectroniksAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_two', 'description', 'description_two', 'description_three', 'client_visit', 'image', 'image_two', 'image_three', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Shop_Board)
class Shop_BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_two', 'description', 'description_two', 'description_three', 'client_visit', 'image', 'image_two', 'image_three', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Shop_Electro_Transport)
class Shop_Electro_TransportAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_two', 'description', 'description_two', 'description_three', 'client_visit', 'image', 'image_two', 'image_three', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Shop_Bcm)
class Shop_BcmAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_two', 'description', 'description_two', 'description_three', 'client_visit', 'image', 'image_two', 'image_three', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Shop_Repair_Operator)
class Shop_Repair_OperatorAdmin(admin.ModelAdmin):
    list_display = ('name', 'name_two', 'description', 'description_two', 'description_three', 'client_visit', 'image', 'image_two', 'image_three', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Shop_Inverter)
class Shop_InverterAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    list_display = ('name', 'name_two', 'description', 'description_two', 'description_three', 'client_visit', 'image', 'image_two', 'image_three', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(BlockCpcFour)
class BlockCpcFourAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget}
    }

    list_display = ('name', 'name_two', 'errors_name', 'errors_name_two', 'errors_name_three', 'errors_name_four', 'errors_name_five', 'errors_name_six',
                    'description', 'description_two', 'description_three', 'description_four', 'description_six', 'description_seven', 'client_visit', 'image', 'image_two', 'image_three',
                    'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения


@admin.register(Favors)
class FavorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'description_two', 'image', 'is_main', 'link', 'price')  # Отображаемые поля в списке брэндов

    def image(self, obj):
        return obj.image.url if obj.image else None  # Отображение превью изображения в админке

    image.short_description = 'Photo Preview'  # Название столбца с превью изображения
