from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Inicio(models.Model):
    pass

class About(models.Model):
    Nosotros = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=500)
    
class Blog(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=40)
    fecha = models.DateField(null - True)
    cuerpo = models.CharField(max_length=3500)
    


    
    
    
    
    
    


    