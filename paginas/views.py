from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class PaginaInicial(TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'paginas\index.html'