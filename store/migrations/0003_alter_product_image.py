# Generated by Django 4.2.8 on 2023-12-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='../static/images/products/'),
        ),
    ]
