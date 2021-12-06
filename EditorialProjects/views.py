from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import *
from .models import *


# Create your views here.
def inicio(request):
    return render(request, 'index.html')


from .Usuario import invitar_usuario
from .Usuario import validar_usuario
from .Usuario import terminar_registro
from .Usuario import modificar_usuario
from .Usuario import cambiar_roles
from .Usuario import desactivar_usuario


def crear_tarea(request):
    formulario = FormularioTarea(request.POST)

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()

    context = {'formulario': formulario}
    return render(request, 'crear-tarea.html', context)
