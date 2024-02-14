from django.contrib import admin
from .models import Grupo, Agenda

@admin.register(Grupo)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('grupo', 'numero')
    search_fields = ['grupo', 'numero']

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('pessoa', 'numero_interno', 'numero_externo')
    search_fields = ['pessoa', 'numero_interno', 'numero_externo']
