from django.contrib import admin

# Register your models here.
from .models import Flan
from .models import ContactForm
from .models import Receta


admin.site.register(Flan)
admin.site.register(ContactForm)
admin.site.register(Receta)