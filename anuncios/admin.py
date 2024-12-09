from django.contrib import admin
from .models import Carro, FotoCarro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco', 'foto_principal')
    search_fields = ('marca', 'modelo')

@admin.register(FotoCarro)
class FotoCarroAdmin(admin.ModelAdmin):
    list_display = ('carro', 'imagem')
