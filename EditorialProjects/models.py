from django.contrib.auth.models import User
from django.db import models

# Expansión del usuario estándar de Django.
class UsuarioBase(models.Model):
    # Vinculación con el usuario base
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    # Declaración de los roles para todos los usuarios
    ADMINISTRADOR = 'AD'
    CORRECTOR = 'CO'
    DISENADOR = 'DI'
    EDITOR = 'ED'
    MAQUETADOR = 'MA'
    TRADUCTOR = 'TR'
    DESACTIVADO = 'NA'
    ROLES_ELEGIBLES = [
        (DESACTIVADO, 'Desactivado'),
        (ADMINISTRADOR, 'Administrador'),
        (CORRECTOR, 'Corrector'),
        (DISENADOR, 'Diseñador'),
        (EDITOR, 'Editor'),
        (MAQUETADOR, 'Maquetador'),
        (TRADUCTOR, 'Traductor'),
    ]

    rol = models.CharField(
        max_length=2,
        choices=ROLES_ELEGIBLES,
        default=DESACTIVADO,
    )

    def __str__(self):
        return self.usuario.username
