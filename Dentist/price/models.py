from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    category = models.ForeignKey(Category,related_name='select_category',on_delete=models.CASCADE) 