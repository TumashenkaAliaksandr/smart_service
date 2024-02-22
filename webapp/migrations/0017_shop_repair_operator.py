# Generated by Django 5.0.1 on 2024-02-22 16:50

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0016_shop_bcm_shop_electro_transport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_Repair_Operator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('name_two', models.CharField(default='Второй Заголовок', max_length=100, verbose_name='name_two')),
                ('description', ckeditor.fields.RichTextField()),
                ('description_two', ckeditor.fields.RichTextField()),
                ('description_three', ckeditor.fields.RichTextField(default='Описание', verbose_name='description three')),
                ('client_visit', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='services', verbose_name='photo')),
                ('image_two', models.ImageField(default='default_image.jpg', upload_to='services', verbose_name='photo_two')),
                ('image_three', models.ImageField(default='default_image_three.jpg', upload_to='services', verbose_name='photo_three')),
                ('is_main', models.BooleanField(default=False)),
                ('link', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Repair of operator panels',
                'verbose_name_plural': 'Repair of operator panels',
            },
        ),
    ]
