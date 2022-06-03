from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from panda1.models import Curso
from panda1.models import Alumnos
from panda1.models import Profesores
from panda1.forms import Cursos
from panda1.forms import Alumnos


def inicio(request):

    return render(request , "app_panda/inicio.html")

def cursos(request):

    if request.method == 'POST':

        miFormulario = Cursos(request.POST)

        print(miFormulario)
    
        if miFormulario.isvalid:
            informacion = miFormulario.cleaned_data

            curso = Curso (curso=informacion['curso'] , codigo=informacion['codigo'])

            curso.save()

            return render(request, "app_panda/inicio.html")

    else:

        miFormulario = Cursos()

def alumnos(request):

    if request.method == 'POST':

        miFormulario = Alumnos(request.POST)

        print(miFormulario)
    
        if miFormulario.isvalid:
            informacion = miFormulario.cleaned_data

            alumno = Alumnos (nombre=informacion['nombre'] , dni=informacion['dni'])

            alumno.save()

            return render(request, "app_panda/inicio.html")

    else:

        miFormulario = Alumnos()
