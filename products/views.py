from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from products.models import Menufacture,Product


class ProductDetailView(DetailView):
    model  = Product
    template_name = "product/product.html"
class ProductListView(ListView):
    model = Product
    template_name = "product/details.html"


# Create your views here.
