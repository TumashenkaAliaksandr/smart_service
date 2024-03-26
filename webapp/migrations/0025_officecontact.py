# Generated by Django 5.0.1 on 2024-03-26 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_blockcpcfour_description_seven_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficeContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('opening_hours', models.CharField(max_length=100)),
            ],
        ),
    ]
