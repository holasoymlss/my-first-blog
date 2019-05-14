from django.db import models
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
import uuid 
from django.contrib.auth.models import User
from datetime import date
from django.template.defaultfilters import slugify

# Create your models here.

class post (models.Model):
    """
    Representa los elementos que forman un post.
    """
    titulo = models.CharField(max_length=200)
    resumen = models.CharField(max_length=200)
    fecha = models.DateField(null=True, blank=True)
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.titulo[:50])
        super(post, self).save(*args, **kwargs)
    
    def __str__(self):
        """
        String que representa al objeto post
        """
        return '%s, %s, %s' % (self.titulo, self.resumen, self.fecha)