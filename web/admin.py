from django.contrib import admin

# Register your models here.
from .models import Flan
from .models import ContactForm


admin.site.register(Flan)
admin.site.register(ContactForm)