from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q

from .models import Agenda

class v_Agenda(ListView):
    paginate_by = 30
    model = Agenda
    template_name = 'agenda/index.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(pessoa__icontains=query) | 
                Q(numero_interno__icontains=query) | 
                Q(numero_externo__icontains=query) | 
                Q(grupo__grupo__icontains=query) |
                Q(grupo__numero__icontains=query) 
            )

        # Ordenar em ordem alfabética
        queryset = queryset.order_by('grupo')
        return queryset
    


#    grupo = models.CharField(max_length=200, verbose_name=_('Grupo'))
#    numero = models.CharField(max_length=5, verbose_name=_('Numero'))

