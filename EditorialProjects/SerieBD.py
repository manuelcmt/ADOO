from django.contrib.auth.models import User
from django.db import models

class Serie(models.Model):
    editor_asignado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=50, unique=True)
    autores = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=300)

    def __str__(self):
        return self.nombre
