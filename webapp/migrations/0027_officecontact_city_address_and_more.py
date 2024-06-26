# Generated by Django 5.0.1 on 2024-04-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0026_blockcpcfour_name_three'),
    ]

    operations = [
        migrations.AddField(
            model_name='officecontact',
            name='city_address',
            field=models.CharField(default='город', max_length=200),
        ),
        migrations.AlterField(
            model_name='officecontact',
            name='address',
            field=models.CharField(default='область', max_length=200),
        ),
        migrations.AlterField(
            model_name='officecontact',
            name='opening_hours',
            field=models.CharField(default='часы работы', max_length=100),
        ),
        migrations.AlterField(
            model_name='officecontact',
            name='phone_number',
            field=models.CharField(default='офис тел', max_length=20),
        ),
    ]
