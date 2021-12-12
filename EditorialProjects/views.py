from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .forms import *
from .decorators import *


# Create your views here.
def inicio(request):
    return render(request, 'index.html')

@para_no_autenticados
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        contrasena = request.POST.get('password')
        usuario = authenticate(request, username=username, password=contrasena)

        if usuario is not None:
            login(request, usuario)
            return redirect('inicio')
        else:
            messages.warning(request, 'Esa combinación de usuario y contraseña no está en el sistema.')

    context = {}

    return render(request, 'inicio_sesion.html', context)


def cerrar_sesion(request):
    logout(request)
    return redirect('iniciar-sesion')

from .Usuario import invitar_usuario
from .Usuario import validar_usuario
from .Usuario import terminar_registro
from .Usuario import modificar_usuario
from .Usuario import cambiar_roles
from .Usuario import desactivar_usuario

from .Serie import registrar_serie
from .Serie import consultar_series

from .Proyecto import registrar_proyecto
from .Proyecto import consultar_proyectos_serie

def crear_tarea(request):
    formulario = FormularioTarea(request.POST)

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()

    context = {'formulario': formulario}
    return render(request, 'crear-tarea.html', context)
