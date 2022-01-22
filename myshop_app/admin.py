from django.contrib import admin
from .models import Product, Cart

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'specs', 'image', 'price', 'slug')
    list_display_links = (['title'])
    search_fields = ('title', 'specs', 'image', 'price')
    prepopulated_fields = {'slug':['title']}

class CartAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'product_id', 'count', 'status')
    list_display_links = (['user_id'])
    search_fields = ('user_id', 'product_id')

admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)