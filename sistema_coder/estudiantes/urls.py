from django.urls import path
from estudiantes.views import saludar, segunda_vista, dia_de_hoy, miNombreEs, listar_estudiantes, listar_profesores

urlpatterns = [
    path("saludar/", saludar),
    path("segundavista/", segunda_vista),
    path("diadehoy/", dia_de_hoy),
    path("minombrees/<nombre>",miNombreEs),
    path("listaestudiantes/", listar_estudiantes),
    path("listaprofesores/", listar_profesores),

]