# Generated by Django 3.1.3 on 2021-12-29 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_shop_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='price',
            field=models.FloatField(),
        ),
    ]
