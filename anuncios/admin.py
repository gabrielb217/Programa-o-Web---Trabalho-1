from django.contrib import admin
from .models import Carro, FotoCarro

@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco', 'vendedor')

admin.site.register(FotoCarro)
