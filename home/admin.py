from django.contrib import admin
from home.models import grafico, valores_grafico

# Register your models here.
class ListandoGrafico(admin.ModelAdmin):
    list_display = ('user', 'name', 'data_criacao', 'data_edicao')

admin.site.register(grafico, ListandoGrafico)
admin.site.register(valores_grafico)