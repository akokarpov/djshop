
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    '''Product in the catalog'''
    title = models.CharField(max_length=50)
    specs = models.TextField(max_length=1000)
    image = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('myshop_app:product', kwargs={'slug' : self.slug})

class Cart(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    status = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'cart items'
        verbose_name = 'item'
    
    def __str__(self):
        return f'{self.user_id}:{self.product_id.title}:{self.count}:{self.status}'
    
    def add_count(self, count):
        self.count = count
        self.save()
        return
    
    def delete(self, using, keep_parents):
        return super().delete(using, keep_parents)
    
    def total(self):
        return self.product_id.price * self.count
    
    def grandtotal(cart_items):
        cart_grandtotal = 0
        for item in cart_items:
            cart_grandtotal += item.total()
        return cart_grandtotal