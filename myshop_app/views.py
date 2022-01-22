from django.http.response import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import Product, Cart
from .forms import ProductForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['page_title'] = 'About'
        return context

class ProductsView(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Products'
        return context

class ProductView(DetailView):
    model = Product
    template_name = "product.html"
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.title
        return context

class CartView(ListView):
    model = Cart
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        cart_items = self.object_list.filter(user_id=user_id)
        grandtotal = self.model.grandtotal(cart_items)
        context['page_title'] = 'Cart'
        context['cart_items'] = cart_items
        context['grandtotal'] = grandtotal
        return context
    
    def post(self, request, *args, **kwargs):
        if request.POST.get('change_count'):
            cart_items = self.model.objects.all()
            cart_item = cart_items.get(id=request.POST.get('item_id'))
            cart_item.add_count(int(request.POST.get('change_count')))
            cart_items = cart_items.filter(user_id=self.request.user.id)
            response = {
                'grandtotal': self.model.grandtotal(cart_items),
                'total': cart_item.total(),
            }
            return JsonResponse(response)

class AddProduct(CreateView):
    form_class = ProductForm
    template_name = 'add_product.html'
    success_url = reverse_lazy('myshop_app:add_product')
    initial = {'image': 'filename'}

    def form_valid(self, form):
        form.clean()
        form.save_image()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('myshop_app:about')
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Add Product'
        return context