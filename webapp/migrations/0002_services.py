# Generated by Django 5.0.1 on 2024-02-10 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(upload_to='services', verbose_name='photo')),
                ('is_main', models.BooleanField(default=False)),
                ('link', models.URLField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
