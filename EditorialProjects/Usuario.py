from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.contrib import messages
from .decorators import *

from .UsuarioBD import *
from .forms import FormularioRegistro
from .Proyecto import consultar_tareas

normalizar = lambda x: False if x == None else True


def invitar_usuario(request):
    if request.method == 'POST':
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

        redirect('invitar-usuario')  # Solo sirve para actualizar la vista y que se vea el mensaje de éxito.

    return render(request, 'UsuarioIH/invitar_usuario.html')


def validar_usuario(request):
    if request.method == 'POST':
        try:
            invitacion = InvitacionUsuario.objects.get(
                correo=request.POST.get('email'))  # Buscamos una invitación para el correo introducido en la interfaz

        except InvitacionUsuario.DoesNotExist:
            messages.error(request, "Invitación inválida.")
            return redirect('/validar-usuario/')

        except InvitacionUsuario.MultipleObjectsReturned:
            invitacion = InvitacionUsuario.objects.filter(correo=request.POST.get('email')).first()

        return redirect('/terminar-registro/{}'.format(invitacion.id))

    return render(request, 'UsuarioIH/validar_usuario.html')


def terminar_registro(request, pk):
    invitacion = InvitacionUsuario.objects.get(id=pk)
    registro = FormularioRegistro(request.POST)

    # Configuración del formulario
    registro.fields['username'].widget.attrs['placeholder'] = "Nombre de usuario"
    registro.fields['username'].widget.attrs['class'] = "form-control"

    registro.fields['email'].widget.attrs['value'] = invitacion.correo
    registro.fields['email'].widget.attrs['class'] = "form-control"
    registro.fields['email'].widget.attrs['readonly'] = True

    registro.fields['first_name'].widget.attrs['placeholder'] = "Su nombre propio"
    registro.fields['first_name'].widget.attrs['value'] = invitacion.nombre
    registro.fields['first_name'].widget.attrs['class'] = "form-control"

    registro.fields['last_name'].widget.attrs['placeholder'] = "Su apellido"
    registro.fields['last_name'].widget.attrs['value'] = invitacion.apellido
    registro.fields['last_name'].widget.attrs['class'] = "form-control"

    registro.fields['password1'].widget.attrs['placeholder'] = "Contraseña"
    registro.fields['password1'].widget.attrs['class'] = "form-control"
    registro.fields['password2'].widget.attrs['placeholder'] = "Contraseña (confirme)"
    registro.fields['password2'].widget.attrs['class'] = "form-control"

    if registro.is_valid():
        if normalizar(request.POST.get('accept_terms')):
            registro.save()
            messages.success(request, 'Su cuenta se ha creado.')
            return redirect('inicio')

        else:
            messages.error(request, 'Debe aceptar los términos y condiciones.')
            redirect('terminar-registro/{}'.format(invitacion.id))

    context = {'nombre': invitacion.nombre, 'apellido': invitacion.apellido, 'correo': invitacion.correo,
               'formulario': registro}
    return render(request, 'UsuarioIH/terminar_registro.html', context)


def modificar_usuario(request):
    try:
        usuarios = User.objects.all()

    except User.DoesNotExist:
        usuarios = None
        messages.error(request, "No hay usuarios registrados.")

    context = {'usuarios': usuarios}
    return render(request, 'UsuarioIH/modificar_usuario.html', context)


def actualizar_permisos_roles(id):
    usuario = User.objects.get(id=id)

    if usuario.usuariobase.es_administrador:
        usuario.groups.add(Group.objects.get(name='Administradores'))

    if usuario.usuariobase.es_corrector:
        usuario.groups.add(Group.objects.get(name='Correctores'))

    if usuario.usuariobase.es_disenador:
        usuario.groups.add(Group.objects.get(name='Diseñadores'))

    if usuario.usuariobase.es_editor:
        usuario.groups.add(Group.objects.get(name='Editores'))

    if usuario.usuariobase.es_maquetador:
        usuario.groups.add(Group.objects.get(name='Maquetadores'))

    if usuario.usuariobase.es_traductor:
        usuario.groups.add(Group.objects.get(name='Traductores'))

    usuario.save()

    return


def cambiar_roles(request, pk):
    usuario = User.objects.get(id=pk)

    if request.method == 'POST':
        usuario.usuariobase.es_administrador = normalizar(request.POST.get('es_administrador'))
        usuario.usuariobase.es_corrector = normalizar(request.POST.get('es_corrector'))
        usuario.usuariobase.es_disenador = normalizar(request.POST.get('es_disenador'))
        usuario.usuariobase.es_editor = normalizar(request.POST.get('es_editor'))
        usuario.usuariobase.es_maquetador = normalizar(request.POST.get('es_maquetador'))
        usuario.usuariobase.es_traductor = normalizar(request.POST.get('es_traductor'))

        usuario.usuariobase.save()
        actualizar_permisos_roles(usuario.id)

        messages.success(request, "Los roles del usuario se han actualizado.")

        redirect('cambiar-roles/{}'.format(
            usuario.id))  # Solo sirve para actualizar la vista y que se vea el mensaje de éxito.

    context = {'usuario': usuario}
    return render(request, 'UsuarioIH/cambiar_roles.html', context)


def desactivar_usuario(request, pk):
    usuario = User.objects.get(id=pk)
    tareas_asignadas = consultar_tareas(request, usuario.id)

    if tareas_asignadas:
        messages.warning(request, "No se puede desactivar un usuario con tareas en proceso.")

    if request.method == 'POST':
        if normalizar(request.POST['confirmacion']):
            usuario.is_active = False
            usuario.save()
            messages.success(request, "El usuario fue desactivado.")
            redirect('modificar-usuario')

    context = {'usuario': usuario, 'tareas': tareas_asignadas}
    return render(request, 'UsuarioIH/desactivar_usuario_confirmacion.html', context=context)
