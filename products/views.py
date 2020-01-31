from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from products.models import Menufacture,Product
from django.http import JsonResponse


# class ProductDetailView(DetailView):
#     model  = Product
#     template_name = "product/product.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         return context
# class ProductListView(ListView):
#     model = Product
#     template_name = "product/details.html"
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
        
#         return context


# Create your views here.
#tins views are only worksea on Api 

def ApiProduct(request):

    product = Product.objects.all()
    data  = {
        "product":list(product.values())
    }
    respons = JsonResponse(data)

    return respons

def ApiProductDitais(request,pk):
    product = Product.objects.get(pk=pk)
    try:
        data = {
            
                'Product Datails':{
                    'name':product.name,
                }
            
        }
        respones = JsonResponse(data)
        return respones
    except product.DoesNotExist:
        data ={
            "error":'404 Page Not Founds'
        }
        respones = JsonResponse(data)
        return respones
