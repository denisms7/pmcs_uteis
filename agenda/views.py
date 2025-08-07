from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q

from unidecode import unidecode

from .models import Agenda

class v_Agenda(ListView):
    paginate_by = 30
    model = Agenda
    template_name = 'agenda/index.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        if query is not None:
            queryS = unidecode(query)
        else:
            # Tratar o caso em que o texto é None
            queryS = query



        
        if query:
            queryset = queryset.filter(
                Q(pessoa__icontains=queryS) | 
                Q(numero_interno__icontains=queryS) | 
                Q(numero_externo__icontains=queryS) | 
                Q(grupo__grupo__icontains=queryS) |
                Q(grupo__numero__icontains=queryS) 
            )

        # Ordenar em ordem alfabética
        queryset = queryset.order_by('grupo')
        return queryset
    


#    grupo = models.CharField(max_length=200, verbose_name=_('Grupo'))
#    numero = models.CharField(max_length=5, verbose_name=_('Numero'))

class v_Exporta(ListView):
    model = Agenda
    template_name = 'agenda/exportacao.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        # Ordenar em ordem alfabética
        queryset = queryset.order_by('grupo')
        return queryset
    