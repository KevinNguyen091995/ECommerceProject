# Generated by Django 4.2.7 on 2023-11-14 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_date_listed'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='currently_listed',
            field=models.BooleanField(default=True),
        ),
    ]
