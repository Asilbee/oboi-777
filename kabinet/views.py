from django.shortcuts import render
from kabinet.models import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hi {username}, siz mofaqiyatli ulandiz !!")
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'd_2/register.html', {'form': form})


def index(request):
    dashboard = Categoriya.objects.all()
    mine_dashboard = Product.objects.all()
    context = {
        'dashboard': dashboard,
        'mine_dashboard': mine_dashboard,
    }
    return render(request, 'admin_2/index.html', context)


def product(request, id):
    product1 = Product_info.objects.filter(last_name_id=id)
    dashboard = Categoriya.objects.all()
    mine_dashboard = Product.objects.all()
    ctx = {
        'product1': product1,
        'dashboard': dashboard,
        'mine_dashboard': mine_dashboard
    }
    return render(request, 'admin_2/product.html', ctx)
