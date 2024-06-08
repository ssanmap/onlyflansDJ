from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Flan
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ContactFormForm
from .forms import LoginForm
from .models import ContactForm
from .models import Receta
# se agregan estas dos para insertar
from .forms import FlanForm
from .models import Flan
import sweetify


def index(request):
    flanes_publicos = Flan.objects.filter(is_private=False)
     # Filtrar los flanes públicos si se proporciona un término de búsqueda
    search_query = request.GET.get('search_query')
    if search_query:
        flanes_publicos = flanes_publicos.filter(name__icontains=search_query)
    return render(request, 'index.html', {'flanes': flanes_publicos})

def about(request):
    company_info = {
        'name': 'ONLYFlans S.A.',
        'description': 'Somos una empresa dedicada a la venta de productos de calidad',
        'creation_date': '1 de enero de 2024',
    }
    return render(request, 'about.html', {'company_info': company_info})

@login_required
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
            sweetify.success(request, '¡Éxito!', text='Tu mensaje ha sido enviado con éxito.')
            return HttpResponseRedirect('/exito')
    else:
        form = ContactFormForm()
    
    return render(request, 'contacto.html', {'form': form})

def exito(request):
    return render(request, 'exito.html')

def recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas.html', {'recetas': recetas})    

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                sweetify.success(request, '¡Éxito!', text='Te has logeado con éxito.')
                return redirect('welcome')
            else:
                form.add_error(None, 'Nombre de usuario o contraseña incorrectos.')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    sweetify.success(request, '¡Éxito!', text='Has cerrado sesión con éxito.')
    return render(request, 'registration/logout.html')

@login_required
def crear_flan(request):
    if request.method == 'POST':
        form = FlanForm(request.POST)
        if form.is_valid():
            form.save()
            sweetify.success(request, '¡Éxito!', text='El flan ha sido creado con éxito.')
            return redirect('index')  
    else:
        form = FlanForm()
    return render(request, 'crear_flan.html', {'form': form})