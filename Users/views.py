from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account is created successfully!Please Sign In / Log In')
            return redirect("login")
    form = UserRegisterForm
    return render(request, 'Users/register.html', {'form':form})
