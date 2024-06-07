from django import forms
from .models import ContactForm

class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre', max_length=100)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)