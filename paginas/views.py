from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import pandas as pd
from django.conf import settings
from datetime import datetime
from django.shortcuts import render
import os


def Aniversariante():
    caminho = os.path.join(settings.BASE_DIR, 'aniversarios.csv')
    print(caminho)
    if os.path.exists(caminho):
        df = pd.read_csv(caminho, encoding='latin1', delimiter=";")
        df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
        filtro = (df['data'].dt.day == datetime.now().day) & (df['data'].dt.month == datetime.now().month)
        aniversariantes_do_dia = df[filtro]
        data = aniversariantes_do_dia.values.tolist()
        return data


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Aniversariante()
        return context

class InteligenciaA(TemplateView):
    template_name = 'paginas/inteligencia_a.html'

class PDM(TemplateView):
    template_name = 'paginas/leis_pdm.html'


class HinoNacional(TemplateView):
    template_name = 'paginas/hinos/hino_nacional.html'

class HinoEstadual(TemplateView):
    template_name = 'paginas/hinos/hino_estadual.html'

class HinoMunicipal(TemplateView):
    template_name = 'paginas/hinos/hino_municipal.html'

class EnderecoOficiais(TemplateView):
    template_name = 'paginas/endereco_oficial/enderecos.html'

class Sismel(TemplateView):
    template_name = 'paginas/sismel.html'

class Atalhos(TemplateView):
    template_name = 'paginas/atalhos.html'

class Speed_test(TemplateView):
    template_name = 'paginas/speed_test.html'




'''
def error_400_view(request, exception):
    return render(request, 'error.html', {'status_code': 400})

def error_403_view(request, exception):
    return render(request, 'error.html', {'status_code': 403})

def error_404_view(request, exception):
    return render(request, 'error.html', {'status_code': 404})

def error_500_view(request):
    return render(request, 'error.html', {'status_code': 500})

def error_502_view(request):
    return render(request, 'error.html', {'status_code': 502})

'''