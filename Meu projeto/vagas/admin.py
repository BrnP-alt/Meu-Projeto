from django.contrib import admin
from .models import Vaga # type: ignore

@admin.register(Vaga)
class VagaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo', 'ocupada')  # Mostra colunas na interface
    list_filter = ('ocupada', 'tipo')  # Adiciona filtros laterais
    search_fields = ('numero',)  # Campo de busca
