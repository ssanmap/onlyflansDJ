from django import forms
from .models import ContactForm
from .models import Flan

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    #  flan agregado  07 junio
class FlanForm(forms.ModelForm):
    class Meta:
        model = Flan
        fields = ['name', 'description', 'image_url', 'slug', 'is_private']   