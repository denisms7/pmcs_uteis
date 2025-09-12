from django.views.generic import TemplateView


class PaginaInicial(TemplateView):
    template_name = 'paginas/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = None
        return context

class InteligenciaA(TemplateView):
    template_name = 'paginas/inteligencia_a.html'

class PDM(TemplateView):
    template_name = 'paginas/leis_pdm.html'

class EnderecoOficiais(TemplateView):
    template_name = 'paginas/endereco_oficial/enderecos.html'

class Speed_test(TemplateView):
    template_name = 'paginas/speed_test.html'
