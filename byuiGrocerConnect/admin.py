from django.contrib import admin
from .models import Product, Customer, Order, OrderItem, Store, Inventory
# Register your models here.

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Store)
admin.site.register(Inventory)