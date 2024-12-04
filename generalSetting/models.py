from django.db import models

# Create your models here.

class GeneralSetting(models.Model):
    site_name = models.CharField(max_length=255,null=False)
    site_logo = models.ImageField(upload_to='site/',null=False,blank=False)
    address   = models.CharField(max_length=255,null=False)
    phone     = models.CharField(max_length=20,null=False)
    email     = models.CharField(max_length=255,null=False)
    footer_text= models.CharField(max_length=300)
    
    
    class Meta:
        db_table = "general_settings"
    