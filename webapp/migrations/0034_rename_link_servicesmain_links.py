# Generated by Django 5.0.1 on 2024-05-24 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0033_alter_servicesmain_h1_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicesmain',
            old_name='link',
            new_name='links',
        ),
    ]