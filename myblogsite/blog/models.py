from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid 
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class post (models.Model):
    """
    Representa los elementos que forman un post.
    """
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=200)
    fecha = models.DateField(null=True, blank=True)
	

    
    def __str__(self):
        """
        String que representa al objeto post
        """
        return '%s, %s, %s' % (self.titulo, self.resumen, self.fecha)