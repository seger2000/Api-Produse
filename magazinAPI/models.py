from django.db import models

# Create your models here.
class Produse(models.Model):
    nume = models.CharField(max_length=100)
    sku = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    description = models.CharField(max_length=100)