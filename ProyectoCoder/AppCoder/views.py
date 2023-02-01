from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from AppCoder.models import Curso

def curso(self):

    curso = Curso(nombre = "Javascript", camada = "19881")
    curso.save()
    documentoDeTexto = f"--->Curso:{curso.nombre}, Camada:{curso.camada}"
    return HttpResponse(documentoDeTexto)