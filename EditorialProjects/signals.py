from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import UsuarioBase, InvitacionUsuario


def nuevo_registro(sender, instance, created, **kwargs):
    if created:
        usuario = UsuarioBase.objects.create(usuario=instance)

        invitacion = InvitacionUsuario.objects.filter(correo=instance.email)

        if invitacion.es_administrador:
            instance.groups.add(Group.objects.get(name='Administradores'))
            usuario.es_administrador = True

        if invitacion.es_corrector:
            instance.groups.add(Group.objects.get(name='Correctores'))
            usuario.es_corrector = True

        if invitacion.es_disenador:
            instance.groups.add(Group.objects.get(name='Diseñadores'))
            usuario.es_disenador = True

        if invitacion.es_editor:
            instance.groups.add(Group.objects.get(name='Editores'))
            usuario.es_aditor = True

        if invitacion.es_maquetador:
            instance.groups.add(Group.objects.get(name='Maquetadores'))
            usuario.es_maquetador = True

        if invitacion.es_traductor:
            instance.groups.add(Group.objects.get(name='Traductores'))
            usuario.es_traductor = True

        usuario.save()

        invitacion.delete()


post_save.connect(nuevo_registro, sender=User)
