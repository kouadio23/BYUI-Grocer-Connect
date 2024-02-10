from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

from byuiGrocerConnect.models import Product

# Create your views here.
def index(request):
    return render(request, "byuiGrocerConnect/base.html", {})

def home(request):
    products = Product.objects.filter(is_featured=True)  # or however you determine featured products
    return render(request, "byuiGrocerConnect/home.html", {'products': products})

def features(request):
    products = Product.objects.filter(is_featured=True)  # or however you determine featured products
    return render(request, "byuiGrocerConnect/features.html", {'products': products})

def aboutUs(request):
    return render(request, "byuiGrocerConnect/aboutUs.html", {})

def contactUs(request):
    return render(request, "byuiGrocerConnect/contactUs.html", {})