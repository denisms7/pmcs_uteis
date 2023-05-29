from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class PaginaInicial(TemplateView):
    template_name = 'paginas\index.html'

class InteligenciaA(TemplateView):
    template_name = 'paginas\inteligencia_a.html'

class PDM(TemplateView):
    template_name = 'paginas\leis_pdm.html'


class HinoNacional(TemplateView):
    template_name = 'paginas\hinos\hino_nacional.html'

class HinoEstadual(TemplateView):
    template_name = 'paginas\hinos\hino_estadual.html'

class HinoMunicipal(TemplateView):
    template_name = 'paginas\hinos\hino_municipal.html'