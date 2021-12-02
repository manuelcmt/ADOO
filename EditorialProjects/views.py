from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import *
from .models import *


# Create your views here.
def inicio(request):
    return render(request, 'index.html')


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
        redirect('invitar-usuario')

    return render(request, 'invitar_usuario.html')


def terminar_registro(request):
    if request.method == 'POST':
        invitacion = InvitacionUsuario.objects.get(correo=request.POST.get('email'))
        if(invitacion):
            return redirect('/captura-registro/{}'.format(invitacion.id))

    return render(request, 'terminar_registro.html')


def captura_registro(request, pk):
    invitacion = InvitacionUsuario.objects.get(id=pk)
    registro = FormularioRegistro(request.POST)
    normalizar = lambda x: False if x == None else True

    if registro.is_valid():
        if normalizar(request.POST.get('accept_terms')):
            registro.save()
            messages.success(request, 'Su cuenta se ha creado.')
            return redirect('inicio')

    context = {'nombre': invitacion.nombre, 'apellido': invitacion.apellido, 'correo': invitacion.correo, 'formulario': registro}
    return render(request, 'registro_usuario.html', context)


def crear_tarea(request):
    formulario = FormularioTarea(request.POST)

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.save()

    context = {'formulario': formulario}
    return render(request, 'crear-tarea.html', context)
