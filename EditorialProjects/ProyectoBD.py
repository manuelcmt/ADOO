from django.contrib.auth.models import User
from django.db import models
from .SerieBD import Serie


class Proyecto(models.Model):
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=50, blank=True)
    no_entrega = models.PositiveIntegerField(unique=True, null=True)

    def __str__(self):
        return self.serie.nombre + ': ' + self.nombre


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

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True)
    encargado = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    CORRECTOR = 'CO'
    DISENADOR = 'DI'
    MAQUETADOR = 'MA'
    TRADUCTOR = 'TR'

    TIPOS_TAREAS = [
        (CORRECTOR, 'Corrección'),
        (DISENADOR, 'Diseño'),
        (MAQUETADOR, 'Maquetación'),
        (TRADUCTOR, 'Traducción'),
    ]

    tipo = models.CharField(
        max_length=2,
        choices=TIPOS_TAREAS,
    )

    def __str__(self):
        return self.proyecto.serie.nombre + ': ' + self.proyecto.no_entrega + ' ' + self.proyecto.nombre + ': ' + self.tipo
