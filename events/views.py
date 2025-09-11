from django.views.generic import TemplateView
from django.utils.translation import get_language
from .calc import get_events


class CalendarTemplateView(TemplateView):
    template_name = 'events/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGE_CODE'] = get_language()
        context['get_events'] = get_events()
        return context
