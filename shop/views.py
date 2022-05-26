from .models import Shop
from django.views.generic import ListView, DetailView

class ProductView(ListView):
    model = Shop
    template_name = 'shop/landing_page.html'
    context_object_name = 'landing_page'

class Product_DetailView(DetailView):
    model = Shop
    template_name = 'shop/product_detail.html'
    context_object_name = 'post'
