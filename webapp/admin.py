from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo_preview')  # Отображаемые поля в списке брэндов

    def photo_preview(self, obj):
        return obj.photo.url if obj.photo else None  # Отображение превью изображения в админке

    photo_preview.short_description = 'Photo Preview'  # Название столбца с превью изображения
