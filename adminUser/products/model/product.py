from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150,unique=True)
    image = models.ImageField(upload_to='products/images/',blank=True,null=True)
    sku=   models.CharField(unique=True,max_length=150)
    
    class Meta:
        db_table = 'products' 
