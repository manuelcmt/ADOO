from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from .ProyectoBD import Tarea
from .SerieBD import Serie
from .ProyectoBD import Proyecto, Tarea


class FormularioRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password1',
                  'password2',
                  'last_name',
                  'first_name')


class FormularioTarea(forms.ModelForm):
    entrega = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Tarea
        fields = "__all__"


class FormularioRegistroSerie(forms.ModelForm):

    class Meta:
        model = Serie
        fields = "__all__"


class FormularioRegistroProyecto(forms.ModelForm):

    class Meta:
        model = Proyecto
        fields = "__all__"