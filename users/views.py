from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from kabinet.models import *


def home(request):
    categoriya = Categoriya.objects.all()
    product_1 = Product_info.objects.all()

    ctx = {
        'categoriya':categoriya,
        'product_1':product_1
    }
    return render(request, 'users/home.html',ctx)


def dash(r):
    return render(r,'admin_2/index.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Hi {username}, siz mofaqiyatli ulandiz !!")
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def profile(request):
    return render(request, 'users/profile.html')



def search(r):
    categoriya = Categoriya.objects.all()
    product = Product_info.objects.all()
    product_1 = Product_info.objects.all()
    if r.method == "POST":
        search = r.POST['search']
        venues = Product_info.objects.filter(name__contains=search)
        return render(r, 'users/home.html',
                      {'search': search,
                       'venues': venues,
                       'product':product,
                       'product_1':product_1,
                       'categoriya': categoriya})
