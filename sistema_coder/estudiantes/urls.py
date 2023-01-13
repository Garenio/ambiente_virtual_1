from django.urls import path
from estudiantes.views import saludar, segunda_vista, dia_de_hoy, miNombreEs, probandoTemplate

urlpatterns = [
    path("saludar/", saludar),
    path("segundavista/", segunda_vista),
    path("diadehoy/", dia_de_hoy),
    path("minombrees/<nombre>",miNombreEs),
    path("probandotemplate", probandoTemplate)

]