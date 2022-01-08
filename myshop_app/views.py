
from django.shortcuts import redirect, render
from .models import Product
from .forms import ProductForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic import ListView, DetailView

def index(request):
    return render(request, 'myshop_app/about.html', {'template_title': 'About'})

class ProductsView(ListView):
    model = Product
    template_name = "myshop_app/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'template_title': 'Products',
            'products': self.object_list,
        }
        return context

class ProductView(DetailView):
    model = Product
    template_name = "myshop_app/product.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            'template_title': self.object.title,
            'product': self.object,
        }
        return context

def cart(request):
    return render(request, 'myshop_app/cart.html', {'template_title': 'Cart'})

def auth(request):
    return render(request, 'myshop_app/auth.html', {'template_title': 'Login'})

class AdminView(CreateView):
    form_class = ProductForm
    template_name = 'myshop_app/administrator.html'
    success_url = '/administrator/'
    initial = {'image': 'filename'}

    def form_valid(self, form):
        form.clean()
        form.save_image()
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_title'] = 'Admin'
        return context
    
    def get_initial(self):
        return super().get_initial()