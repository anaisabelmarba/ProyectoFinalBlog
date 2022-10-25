from socket import fromshare
from django import forms

class RegistrateFormulario(forms.Form):
    email = forms.CharField(max_length=60)
    contraseña = forms.CharField(max_length=10)
    nombre_usuario = forms.CharField(max_length=30)
    
class BlogFormulario(forms.Form):
    titulo = forms.CharField(max_length=60)
    subtitulo = forms.CharField(max_length=60)
    autor = forms.CharField(max_length=40)
    fecha = forms.DateField(null=True)
    cuerpo = forms.CharField(max_length=3500)
    
class PerfilFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    descripcion = forms.CharField(max_length=100)
    
    
    