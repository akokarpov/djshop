
from django.urls import path
from . import views

app_name = 'myshop_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.ProductsView.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductView.as_view(), name='product'),
    path('cart/', views.cart, name='cart'),
    path('auth/', views.auth, name='auth'),
    path('administrator/', views.AdminView.as_view(), name='administrator'),
]