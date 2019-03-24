from django.contrib import admin
from .models import Project


# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    """ Extenció de configuració base de l'administrador sobreescribint propietats """
    readonly_fields = ('created', 'updated')


# Es registre el model projecte amb la clase ProjectAdmin
admin.site.register(Project, ProjectAdmin)

