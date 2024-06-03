from django.urls import path
from .views import index, about, welcome, contacto, exito

urlpatterns = [
    path('', index, name='index'),
    path('acerca/', about, name='about'),
    path('bienvenido/', welcome, name='welcome'),
    path('contacto/', contacto, name='contacto'),
    path('exito/', exito, name='exito'),
]