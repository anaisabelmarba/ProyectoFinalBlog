from django.db import models

# Create your models here.
class Inicio(models.Model):
    pass


class About(models.Model):
    Nosotros = models.TextField(max_length=300)
    Acerca_de = models.TextField(max_length=500)
       

class Blog(models.Model):
    titulo = models.CharField(max_length=60)
    subtitulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=40)
    fecha = models.DateField(null=True)
    cuerpo = models.TextField(max_length=3500)
    
class Registrate(models.Model):
    email = models.CharField(max_length=60)
    contraseña = models.CharField(max_length=10)
    nombre_usuario = models.CharField(max_length=30)
    
class Perfil(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.TextField(max_length=100)
