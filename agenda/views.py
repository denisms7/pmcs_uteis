from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q
from unidecode import unidecode

from .models import Agenda


class v_Agenda(ListView):
    """
    Lista de agendas com pesquisa por pessoa, número interno/externo ou grupo.
    """
    model = Agenda
    template_name = 'agenda/index.html'
    paginate_by = 30

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q', '')

        # Normaliza a query para ignorar acentos
        query_normalized = unidecode(query) if query else ''

        if query_normalized:
            queryset = queryset.filter(
                Q(pessoa__icontains=query_normalized) |
                Q(numero_interno__icontains=query_normalized) |
                Q(numero_externo__icontains=query_normalized) |
                Q(grupo__grupo__icontains=query_normalized) |
                Q(grupo__numero__icontains=query_normalized)
            )

        return queryset.order_by('grupo')


class v_Exporta(ListView):
    """
    Lista de agendas para exportação, ordenada pelo grupo.
    """
    model = Agenda
    template_name = 'agenda/exportacao.html'

    def get_queryset(self):
        return super().get_queryset().order_by('grupo')
