from django.http import HttpResponse
from django.shortcuts import render
from products.models import Product, Category, Cartridges, ProductBrand

# Create your views here.
def index(request):
    brands = ProductBrand.objects.all()
    context = {
        'brands': brands,
    }
    return render(request, "home/index.html", context )
