
from django.db import models

class Product(models.Model):
    '''Product in the catalog'''
    title = models.CharField(max_length=50)
    specs = models.TextField(max_length=1000)
    image = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title