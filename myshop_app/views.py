
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView

def index(request):
    return render(request, 'about.html', {'page_title': 'About'})

class ProductsView(ListView):
    model = Product
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'page_title': 'Products',
            'products': self.object_list,
        }
        return context

class ProductView(DetailView):
    model = Product
    template_name = "product.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'page_title': self.object.title,
            'product': self.object,
        }
        return context

def cart(request):
    return render(request, 'cart.html', {'page_title': 'Cart'})

def auth(request):
    return render(request, 'auth.html', {'page_title': 'Login'})

class AdminView(CreateView):
    form_class = ProductForm
    template_name = 'administrator.html'
    success_url = '/administrator/'
    initial = {'image': 'filename'}
    extra_context = {'page_title': 'Admin'}

    def form_valid(self, form):
        form.clean()
        form.save_image()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('myshop_app:index')
        return super().get(request, *args, **kwargs)