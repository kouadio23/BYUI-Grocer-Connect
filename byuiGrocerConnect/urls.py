from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('',views.home, name='home'),
    path('features/', views.features, name='features'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('contactUs/', views.contactUs, name='contactUs'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
]
