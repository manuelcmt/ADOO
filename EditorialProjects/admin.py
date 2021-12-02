from django.contrib import admin

# Register your models here.
from EditorialProjects.models import *

admin.site.register(UsuarioBase)
admin.site.register(InvitacionUsuario)
admin.site.register(Tarea)