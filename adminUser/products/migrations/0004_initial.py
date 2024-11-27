# Generated by Django 5.1.3 on 2024-11-27 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('slug', models.CharField(max_length=150, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('sku', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'products',
            },
        ),
    ]