from pyexpat.errors import messages
from urllib import response
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from byuiGrocerConnect.cart import Cart
from byuiGrocerConnect.models import Product



# Create your views here.
def index(request):
    return render(request, "byuiGrocerConnect/base.html", {})

def home(request):
    products = Product.objects.filter(is_featured=True)  # or however you determine featured products
    # pass the products to the template
    return render(request, "byuiGrocerConnect/home.html", {'products': products})

def features(request):
    products = Product.objects.filter(is_featured=True)  # or however you determine featured products
    return render(request, "byuiGrocerConnect/features.html", {'products': products})

def aboutUs(request):
    return render(request, "byuiGrocerConnect/aboutUs.html", {})

def contactUs(request):
    return render(request, "byuiGrocerConnect/contactUs.html", {})


@require_POST
def add_to_cart(request):
    cart = Cart(request)
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))

    try:
        product = Product.objects.get(id=product_id)
        cart.add(product=product, quantity=quantity)
        messages.success(request, 'Product added to cart successfully.')
        return redirect('product_list')
    except Product.DoesNotExist:
        messages.error(request, 'Product not found.')
    except Exception as e:
        messages.error(request, f'Error adding product to cart: {e}')

    return render(request, 'home.html', {'error': 'There was an issue adding the item to your cart.'})