from django.shortcuts import render, redirect
from django.contrib import messages

from .ProyectoBD import Tarea, Proyecto
from .forms import FormularioRegistroProyecto
from .SerieBD import Serie
from .decorators import *


def consultar_tareas(request, id_usuario):
    try:
        tareas = Tarea.objects.filter(encargado_id=id_usuario)
    except Tarea.DoesNotExist:
        tareas = None

    return tareas


def crear_tareas(proyecto):
    Tarea.objects.create(estado=Tarea.NO_ASIGNADA, proyecto=proyecto, tipo=Tarea.CORRECTOR)
    Tarea.objects.create(estado=Tarea.NO_ASIGNADA, proyecto=proyecto, tipo=Tarea.DISENADOR)
    Tarea.objects.create(estado=Tarea.NO_ASIGNADA, proyecto=proyecto, tipo=Tarea.MAQUETADOR)
    Tarea.objects.create(estado=Tarea.NO_ASIGNADA, proyecto=proyecto, tipo=Tarea.TRADUCTOR)


def registrar_proyecto(request):
    formulario = FormularioRegistroProyecto(request.POST)
    series_asignadas = Serie.objects.filter(editor_asignado=request.user.id)

    formulario.fields['no_entrega'].widget.attrs['placeholder'] = "Número de serialización"
    formulario.fields['no_entrega'].widget.attrs['class'] = "form-control"
    formulario.fields['nombre'].widget.attrs['placeholder'] = "Subtítulo de esta entrega"
    formulario.fields['nombre'].widget.attrs['class'] = "form-control"

    if request.method == 'POST':
        if formulario.is_valid():
            formulario.serie = request.POST['serie']
            formulario.save()
            proyecto = Proyecto.objects.get(serie=request.POST['serie'], no_entrega=request.POST['no_entrega'])
            crear_tareas(proyecto)
            messages.success(request, "El proyecto se ha registrado.")
            return redirect('inicio')
        else:
            messages.error(request, "La serie ya existe.")

    context = {'formulario': formulario, 'series_asignadas': series_asignadas}
    return render(request, 'ProyectoIH/registrar_proyecto.html', context)


def consultar_proyectos_serie(request, pk):
    serie = Serie.objects.get(id=pk)
    proyectos = Proyecto.objects.filter(serie=serie)

    if not proyectos:
        messages.warning(request, "No se han registrado proyectos en esta serie.")


    context = {'serie': serie, 'proyectos': proyectos}
    return render(request, 'ProyectoIH/proyectos_serie.html', context)


def es_proyecto_completado(proyecto):
    completado = True

    for tarea in proyecto.tarea_set:
        if tarea.estado != Tarea.COMPLETADA:
            completado = False

    return completado


def es_proyecto_borrador(proyecto):
    borrador = True

    for tarea in proyecto.tarea_set:
        if tarea.estado != Tarea.NO_ASIGNADA:
            borrador = False

    return borrador
