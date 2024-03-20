# Generated by Django 5.0.1 on 2024-03-20 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0021_blockcpcfour'),
    ]

    operations = [
        migrations.AddField(
            model_name='blockcpcfour',
            name='errors_name',
            field=models.CharField(default='Причина Ошибки 1', max_length=100, verbose_name='errors_name'),
        ),
        migrations.AddField(
            model_name='blockcpcfour',
            name='errors_name_five',
            field=models.CharField(default='Причина Ошибки 5', max_length=100, verbose_name='errors_name_five'),
        ),
        migrations.AddField(
            model_name='blockcpcfour',
            name='errors_name_four',
            field=models.CharField(default='Причина Ошибки 4', max_length=100, verbose_name='errors_name_four'),
        ),
        migrations.AddField(
            model_name='blockcpcfour',
            name='errors_name_six',
            field=models.CharField(default='Причина Ошибки 6', max_length=100, verbose_name='errors_name_six'),
        ),
        migrations.AddField(
            model_name='blockcpcfour',
            name='errors_name_three',
            field=models.CharField(default='Причина Ошибки 3', max_length=100, verbose_name='errors_name_three'),
        ),
        migrations.AddField(
            model_name='blockcpcfour',
            name='errors_name_two',
            field=models.CharField(default='Причина Ошибки 2', max_length=100, verbose_name='errors_name_two'),
        ),
    ]