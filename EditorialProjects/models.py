# Expansión del usuario estándar de Django.
from .UsuarioBD import UsuarioBase
from .UsuarioBD import InvitacionUsuario

from .SerieBD import Serie

from .ProyectoBD import Tarea
from .ProyectoBD import Proyecto

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

