from django.contrib import admin
from .models import Agenda_Externa


@admin.register(Agenda_Externa)
class AgendaExternaAdmin(admin.ModelAdmin):
    list_display = ('destino', 'ramal', 'numero_externo')
    search_fields = ['destino', 'numero_externo']
