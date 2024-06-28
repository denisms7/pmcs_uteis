from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.db.models import Q
from datetime import datetime
from django.contrib import messages
from django.db import IntegrityError


from .forms import FormAgendaExterna
from unidecode import unidecode
from .models import Agenda_Externa

class v_AgendaExterna(ListView):
    paginate_by = 30
    model = Agenda_Externa
    template_name = 'agenda_externa/index.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')

        # Filtrando por um campo específico, se a query existir
        if query:
            queryset = queryset.filter(destino__icontains=query)

        # Ordenar em ordem alfabética
        queryset = queryset.order_by('destino')
        return queryset


class AgendaExternaCreateView(CreateView):
    model = Agenda_Externa
    form_class = FormAgendaExterna
    template_name = 'agenda_externa/added.html'
    success_url = reverse_lazy('Agenda_Externa')

    def form_valid(self, form):

        form.instance.data_att = datetime.now()

        try:
            url = super().form_valid(form)
        except IntegrityError as e:
            return self.handle_unique(e)

        messages.success(self.request, "Registro salvo com sucesso.")
        return url

