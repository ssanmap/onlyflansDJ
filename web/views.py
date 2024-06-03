from django.shortcuts import render
from .models import Flan
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactFormForm
from .models import ContactForm

def index(request):
    products = [
        {'name': 'Producto 1', 'price': 10.99},
        {'name': 'Producto 2', 'price': 19.99},
        {'name': 'Producto 3', 'price': 5.99},
        {'name': 'Producto 4', 'price': 10.99},
        {'name': 'Producto 5', 'price': 19.99},
        {'name': 'Producto 6', 'price': 5.99},
        {'name': 'Producto 7', 'price': 10.99},
        {'name': 'Producto 8', 'price': 19.99},
        {'name': 'Producto 9', 'price': 5.99},
        {'name': 'Producto 10', 'price': 10.99},
        {'name': 'Producto 11', 'price': 19.99},
        {'name': 'Producto 12', 'price': 5.99},
        {'name': 'Producto 13', 'price': 10.99},
        {'name': 'Producto 14', 'price': 19.99},
        {'name': 'Producto 15', 'price': 5.99},
        {'name': 'Producto 16', 'price': 10.99},
        {'name': 'Producto 17', 'price': 19.99},
        {'name': 'Producto 18', 'price': 5.99},
        {'name': 'Producto 19', 'price': 10.99},
        {'name': 'Producto 20', 'price': 19.99},
        {'name': 'Producto 21', 'price': 5.99},
        {'name': 'Producto 22', 'price': 10.99},
        {'name': 'Producto 23', 'price': 19.99},
        {'name': 'Producto 24', 'price': 5.99},
        {'name': 'Producto 25', 'price': 10.99},
        {'name': 'Producto 26', 'price': 19.99},
        {'name': 'Producto 27', 'price': 5.99},
        {'name': 'Producto 28', 'price': 10.99},
        {'name': 'Producto 29', 'price': 19.99},
        {'name': 'Producto 30', 'price': 5.99},
    ]
    flanes_publicos = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def about(request):
    company_info = {
        'name': 'SANMARTIN S.A.',
        'description': 'Somos una empresa dedicada a la venta de productos de calidad',
        'creation_date': '1 de enero de 2024',
    }
    return render(request, 'about.html', {'company_info': company_info})

def welcome(request):
    flanes_privados = Flan.objects.filter(is_private=True)
    return render(request, 'welcome.html', {'flanes': flanes_privados})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
        if form.is_valid():
            ContactForm.objects.create(
                customer_email=form.cleaned_data['customer_email'],
                customer_name=form.cleaned_data['customer_name'],
                message=form.cleaned_data['message']
            )
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormForm()
    
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')