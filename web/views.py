from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Flan
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactFormForm
from .models import ContactForm
from .models import Receta


def index(request):
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

def recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas.html', {'recetas': recetas})    