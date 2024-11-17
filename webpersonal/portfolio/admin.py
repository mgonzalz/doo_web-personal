from django.contrib import admin
from .models import Project

# Register your models here.

'''
La fecha de creación se añade automáticamente cuando se crea un proyecto.
La fecha de edición igual.
El siguiente comando permite mostrarlos como campos de tipo 'solo lectura' en el panel de administración de Django.
'''
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)

