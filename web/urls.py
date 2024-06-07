from django.urls import path, include
from django.contrib import admin
from .views import index, about, welcome, contacto, exito, recetas, login, logout

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenido/', welcome, name='welcome'),
    path('contacto/', contacto, name='contacto'),
    path('exito/', exito, name='exito'),
    path('recetas/', recetas, name='recetas'),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
     path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]