from django.urls import path
from EditorialProjects import views

urlpatterns = [
    path('', views.inicio, name="inicio"),

]