from django.views.generic import TemplateView
from generic.models import Category, Button


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday'] = None
        context['category'] = Category.objects.filter(active=True)
        context['button'] = Button.objects.filter()
        return context


class IaTemplateView(TemplateView):
    template_name = 'home/ia.html'


class PDM(TemplateView):
    template_name = 'home/pdm.html'
