from django.shortcuts import render
from django.views.generic.list import ListView
from django.db.models import Q

from .models import Agenda

class v_Agenda(ListView):
    paginate_by = 30
    model = Agenda
    template_name = 'cadastros/pessoa/busca_pessoa.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(primeiro_nome__icontains=query) | Q(cpf__icontains=query)
            )
        return queryset