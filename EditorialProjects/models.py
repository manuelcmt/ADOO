from django.contrib.auth.models import User
from django.db import models


# Expansión del usuario estándar de Django.
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


class Tarea(models.Model):
    NO_ASIGNADA = 'NA'
    ASIGNADA = 'AS'
    EN_PROCESO = 'EP'
    COMPLETADA = 'CO'

    ESTADOS_TAREAS = [
        (NO_ASIGNADA, 'No asignada'),
        (ASIGNADA, 'Asignada'),
        (EN_PROCESO, 'En proceso'),
        (COMPLETADA, 'Completada'),
    ]

    estado = models.CharField(
        max_length=2,
        choices=ESTADOS_TAREAS,
        default=NO_ASIGNADA,
    )

    encargado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    entrega = models.DateField()

    importe = models.DecimalField(decimal_places=2, max_digits=4)

    CORRECTOR = 'CO'
    DISENADOR = 'DI'
    MAQUETADOR = 'MA'
    TRADUCTOR = 'TR'

    TIPOS_TAREAS = [
        (CORRECTOR, 'Corrección'),
        (DISENADOR, 'Diseño'),
        (MAQUETADOR, 'Maquetación'), # 3 min
        (TRADUCTOR, 'Traducción'),
    ]

    tipo = models.CharField(
        max_length=2,
        choices=TIPOS_TAREAS,
    )

