
import email
from django.shortcuts import render
from django.http import HttpResponse
from blog.forms import RegistrateFormulario
from ProyectoFinalBlog.ProyectoFinalBlog.blog.models import Registrate


# Create your views here.
def base(request):
    return render(request, "blog/base.html")

def  registrateFormulario(request):
    if request.method == 'POST':
        miFormulario = RegistrateFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid: 
            informacion = miFormulario.cleaned_data
            registrate = Registrate(email=informacion['email'], contraseña=informacion['contraseña'], nombre_usuario=informacion['nombre_usuario'])
            registrate.save()
            return render(request, "blog/inicio.html")
    else:
        miFormulario= RegistrateFormulario()
    return render(request, "blog/registrateFormulario.html", {"miFormulario":miFormulario})    


def inicio(request):
    return render(request, "blog/inicio.html")

def about(request):
    return render(request, "blog/about.html")

def blog(request):
    return render(request, "blog/blog.html")

def registrate(request):
    return render(request, "blog/registrate.html")

def perfil(request):
    return render(request, "blog/perfil.html")
    



