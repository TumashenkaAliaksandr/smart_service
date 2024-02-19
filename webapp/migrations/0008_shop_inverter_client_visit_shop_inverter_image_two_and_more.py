# Generated by Django 5.0.1 on 2024-02-15 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_shop_inverter'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop_inverter',
            name='client_visit',
            field=models.TextField(default='Выезд к Клиенту', verbose_name='client_visit'),
        ),
        migrations.AddField(
            model_name='shop_inverter',
            name='image_two',
            field=models.ImageField(default='default_image.jpg', upload_to='services', verbose_name='photo_two'),
        ),
        migrations.AddField(
            model_name='shop_inverter',
            name='name_two',
            field=models.CharField(default='Второй Заголовок', max_length=100, verbose_name='name_two'),
        ),
    ]