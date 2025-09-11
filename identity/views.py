from django.views.generic import TemplateView


class NationalTemplateView(TemplateView):
    template_name = 'identity/anthem/national.html'


class StateTemplateView(TemplateView):
    template_name = 'identity/anthem/state.html'


class MunicipalTemplateView(TemplateView):
    template_name = 'identity/anthem/municipal.html'
