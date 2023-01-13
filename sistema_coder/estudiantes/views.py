from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

def saludar(request):
    return HttpResponse(f"Hola Mundo en Django. La hora es {datetime.now()}")

def segunda_vista(request):
    return(HttpResponse("<br><br>Esta es la segunda vista de prueba. Excelente"))

def dia_de_hoy(request):
    dia = datetime.now()
    documentoDeTexto = f"Hoy es día:<br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es {nombre}"
    return HttpResponse(documentoDeTexto)

def probandoTemplate(self):
    miHtml = open("C:\Users\Eugenio\Desktop\Curso Python\Proyectos\ambiente_virtual_1\sistema_coder\plantillas\template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
