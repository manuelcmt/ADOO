from django.shortcuts import render, redirect
from django.contrib import messages

from .SerieBD import *
from .forms import FormularioRegistroSerie

from .decorators import *


def registrar_serie(request):
    editores = User.objects.filter(usuariobase__es_editor=True)
    formulario = FormularioRegistroSerie(request.POST)

    formulario.fields['nombre'].widget.attrs['placeholder'] = "Nombre de la serie"
    formulario.fields['nombre'].widget.attrs['class'] = "form-control"
    formulario.fields['autores'].widget.attrs['placeholder'] = "Liste los autores"
    formulario.fields['autores'].widget.attrs['class'] = "form-control"
    formulario.fields['descripcion'].widget.attrs['placeholder'] = "Escriba una sinopsis o descripción"
    formulario.fields['descripcion'].widget.attrs['class'] = "form-control"
    formulario.fields['descripcion'].widget.attrs['style'] = "height:300px"


    if request.method == 'POST':
        if formulario.is_valid():
            formulario.editor_asignado = request.POST['editor_asignado']
            formulario.save()
            messages.success(request, "La serie se ha registrado.")
            return redirect('inicio')
        else:
            messages.error(request, "La serie ya existe.")

    context = {'formulario': formulario, 'editores': editores}
    return render(request, 'SerieIH/registrar_serie.html', context)


def consultar_series(request):
    try:
        if request.user.usuariobase.es_administrador:
            series = Serie.objects.all()
        else:
            series = Serie.objects.filter(editor_asignado=request.user)

    except Serie.DoesNotExist:
        series = None
        messages.error(request, "No series disponibles.")

    context = {'series': series}
    return render(request, 'SerieIH/consultar_series.html', context)

