from django.contrib.auth.models import User, Group
from django.db import models


class UsuarioBase(models.Model):
    # Vinculación con el usuario base
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    es_administrador = models.BooleanField(default=False)
    es_corrector = models.BooleanField(default=False)
    es_disenador = models.BooleanField(default=False)
    es_editor = models.BooleanField(default=False)
    es_maquetador = models.BooleanField(default=False)
    es_traductor = models.BooleanField(default=False)

    def __str__(self):
        return self.usuario.username


class InvitacionUsuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()

    es_administrador = models.BooleanField()
    es_corrector = models.BooleanField()
    es_disenador = models.BooleanField()
    es_editor = models.BooleanField()
    es_maquetador = models.BooleanField()
    es_traductor = models.BooleanField()