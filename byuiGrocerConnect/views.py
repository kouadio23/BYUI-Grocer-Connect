from django.shortcuts import render
from django.http import HttpResponse

from byuiGrocerConnect.models import Product

# Create your views here.
def index(response):
    return render(response, "byuiGrocerConnect/base.html", {})

def home(response):
    products = Product.objects.filter(is_featured=True)  # or however you determine featured products
    return render(response, "byuiGrocerConnect/home.html", {'products': products})

def features(response):
    products = Product.objects.filter(is_featured=True)  # or however you determine featured products
    return render(response, "byuiGrocerConnect/features.html", {'products': products})