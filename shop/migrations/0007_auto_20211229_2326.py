# Generated by Django 3.1.3 on 2021-12-29 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20211229_2324'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='excerpt',
            new_name='description',
        ),
    ]