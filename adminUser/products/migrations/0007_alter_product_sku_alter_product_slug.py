# Generated by Django 5.1.3 on 2024-11-27 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, unique=True),
        ),
    ]
