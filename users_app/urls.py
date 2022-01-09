
from django.urls import path
from . import views

app_name = 'users_app'

urlpatterns = [
    path('login', views.UserLogin.as_view(), name='login'),
    path('logout', views.UserLogout.as_view(), name='logout'),
]