
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect

class UserLogin(LoginView):
    next_page = 'myshop_app:about'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('myshop_app:about')
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super(UserLogin, self).get_context_data(**kwargs)
        context['page_title'] = 'Login'
        return context

class UserLogout(LogoutView):
    extra_context = {'page_title': "Logout",}

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('myshop_app:about')
        return super().get(request, *args, **kwargs)