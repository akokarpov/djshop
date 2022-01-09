
from django.contrib.auth.views import LoginView, LogoutView 

class UserLogin(LoginView):
    next_page = 'myshop_app:index'
    extra_context = {'page_title': 'Login',}

class UserLogout(LogoutView):
    extra_context = {'page_title': "Logout",}