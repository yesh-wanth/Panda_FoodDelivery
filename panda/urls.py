from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('', views.Home, name='home'),
]