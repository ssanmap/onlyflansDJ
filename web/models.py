import uuid
from django.db import models

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField(unique=True)
    is_private = models.BooleanField(default=False)
     # Campo nuevo
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()

    def __str__(self):
        return self.customer_name

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    instrucciones = models.TextField()

    def __str__(self):
        return self.nombre        