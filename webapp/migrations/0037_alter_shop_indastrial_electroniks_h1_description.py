# Generated by Django 5.0.1 on 2024-05-24 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0036_alter_shop_indastrial_electroniks_h1_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_indastrial_electroniks',
            name='h1_description',
            field=models.TextField(default='Описание', max_length=250, verbose_name='h1_description'),
        ),
    ]