from django.db import models

# Create your models here.
class Item(models.Model):
   id = models.BigAutoField(primary_key=True) 
   name = models.CharField(max_length=200, null=True)
   stock = models.IntegerField(default=0, null=True, blank=True)
   price = models.IntegerField(default=0, null=True, blank=True)
   item_type = models.CharField(max_length=200, null=True, blank=True)
   image = models.ImageField(upload_to='media/', null=True)
   
   
   def __str__(self):
        return str(self.name) 