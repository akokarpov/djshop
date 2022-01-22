
from django.urls import path
from . import views

app_name = 'myshop_app'

urlpatterns = [
    path('', views.AboutView.as_view(), name='about'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/<slug:slug>/', views.ProductView.as_view(), name='product'),
    path('add_product/', views.AddProduct.as_view(), name='add_product'),
    path('cart/', views.CartView.as_view(), name='cart'),
]