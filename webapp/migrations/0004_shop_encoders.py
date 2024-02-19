# Generated by Django 5.0.1 on 2024-02-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_services_description_two'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop_Encoders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('description_two', models.TextField(default='Описание', verbose_name='description_two')),
                ('image', models.ImageField(upload_to='services', verbose_name='photo')),
                ('is_main', models.BooleanField(default=False)),
                ('link', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Encoders',
                'verbose_name_plural': 'Encoders',
            },
        ),
    ]