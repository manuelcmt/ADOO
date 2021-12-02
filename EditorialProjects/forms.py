from django.contrib.auth.forms import UserCreationForm
from django import forms

from EditorialProjects.models import *


class FormularioRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2',
                  'last_name',
                  'first_name']


class FormularioTarea(forms.ModelForm):
    entrega = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        model = Tarea
        fields = "__all__"