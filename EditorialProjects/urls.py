from django.urls import path
from EditorialProjects import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('iniciar-sesion', views.iniciar_sesion, name="iniciar-sesion"),
    path('cerrar-sesion', views.cerrar_sesion, name="cerrar-sesion"),

]