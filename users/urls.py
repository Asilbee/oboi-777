from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .views import search,dash
from kabinet.views import *


urlpatterns = [
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('dashboard/', index, name='dash'),
    path('search', search, name="search"),
    path('product/<int:id>/', product, name='product'),
    path('', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/login.html'), name="logout"),
]
