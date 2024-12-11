from django.db import models
from django.utils.text import slugify

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    
# Attribute Model
class Attribute(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)

    class Meta:
        db_table = 'attributes'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)  
    slug = models.SlugField(max_length=150, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='products/images/', blank=True, null=True)
    sku = models.CharField(max_length=150, unique=True,blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
        db_table = 'products'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# ProductAttribute Model
class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attributes')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, null=True, blank=True, related_name='product_attributes')
    attribute_value = models.CharField(max_length=255, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    class Meta:
        db_table = 'product_attributes'

    def __str__(self):
        return f"{self.product.name} - {self.attribute.name} ({self.attribute_value})"

