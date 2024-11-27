from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150,unique=True,blank=True, null=True)
    image = models.ImageField(upload_to='products/images/',blank=True,null=True)
    sku=   models.CharField(unique=True,max_length=150)
    description = models.TextField(max_length=2000,blank=True,null=True)
    class Meta:
        db_table = 'products' 
        
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        super(Product, self).save(*args, **kwargs)