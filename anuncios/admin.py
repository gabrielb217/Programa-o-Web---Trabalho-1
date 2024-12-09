from django.contrib import admin
from .models import Carro, FotoCarro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco', 'foto_principal')
    list_filter = ('marca', 'ano')
    search_fields = ('marca', 'modelo')
    actions = ['delete_selected'] 

@admin.register(FotoCarro)
class FotoCarroAdmin(admin.ModelAdmin):
    list_display = ('carro', 'imagem')
    actions = ['delete_selected']