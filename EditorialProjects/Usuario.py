from django.contrib.auth.models import User
from django.db import models

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import FormularioRegistro

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


def validar_usuario(request):
    if request.method == 'POST':
        try:
            invitacion = InvitacionUsuario.objects.get(correo=request.POST.get('email'))  # Buscamos una invitación para el correo introducido en la interfaz

        except InvitacionUsuario.DoesNotExist:
            messages.error(request, "Invitación inválida.")
            return redirect('/validar-usuario/')

        except InvitacionUsuario.MultipleObjectsReturned:
            invitacion = InvitacionUsuario.objects.filter(correo=request.POST.get('email')).first()

        return redirect('/terminar-registro/{}'.format(invitacion.id))

    return render(request, 'UsuarioIH/validar_usuario.html')


def invitar_usuario(request):
    if request.method == 'POST':
        normalizar = lambda x: False if x == None else True
        invitacion = InvitacionUsuario.objects.create(
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            correo=request.POST.get('correo'),
            es_administrador=normalizar(request.POST.get('es_administrador')),
            es_corrector=normalizar(request.POST.get('es_corrector')),
            es_disenador=normalizar(request.POST.get('es_disenador')),
            es_editor=normalizar(request.POST.get('es_editor')),
            es_maquetador=normalizar(request.POST.get('es_maquetador')),
            es_traductor=normalizar(request.POST.get('es_traductor')))

        invitacion.save()
        messages.success(request, "La invitación se ha creado correctamente.")

        redirect('invitar-usuario') #Solo sirve para actualizar la vista y que se vea el mensaje de éxito.

    return render(request, 'UsuarioIH/invitar_usuario.html')


def terminar_registro(request, pk):
    invitacion = InvitacionUsuario.objects.get(id=pk)
    registro = FormularioRegistro(request.POST)
    normalizar = lambda x: False if x == None else True

    if registro.is_valid():
        if normalizar(request.POST.get('accept_terms')):
            registro.save()
            messages.success(request, 'Su cuenta se ha creado.')
            return redirect('inicio')

    context = {'nombre': invitacion.nombre, 'apellido': invitacion.apellido, 'correo': invitacion.correo,
               'formulario': registro}
    return render(request, 'UsuarioIH/terminar_registro.html', context)


def modificar_usuario(request):
    try:
        usuarios = User.objects.all()

    except User.DoesNotExist:
        usuarios = None

    context = {'usuarios': usuarios}
    return render(request, 'UsuarioIH/modificar_usuario.html', context)


def cambiar_roles(request, pk):
    return redirect('inicio')


def desactivar_usuario(request, pk):
    return redirect('inicio')


