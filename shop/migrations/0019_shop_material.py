# Generated by Django 4.0.4 on 2022-05-26 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_rename_description_shop_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='material',
            field=models.TextField(default='N/A', max_length=200),
        ),
    ]
