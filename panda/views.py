from django.shortcuts import render, redirect
from .models import FoodItem
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = FoodItem.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = FoodItem.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = FoodItem.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = FoodItem.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")

# Create your views here.
def Home(request):
    context = {
        'foods': FoodItem.objects.all()
    }
    return render(request, 'panda/home.html', context)

def cart(request):
    return render(request, 'panda/cart_details.html')
