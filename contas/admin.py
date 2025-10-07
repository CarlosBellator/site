from django.contrib import admin
from contas.models import userProfile as Perfil

# Register your models here.
class ListandoPerfil(admin.ModelAdmin):
    list_display = ('user', 'foto_perfil')

admin.site.register(Perfil, ListandoPerfil)