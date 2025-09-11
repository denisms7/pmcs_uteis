from django.views.generic import TemplateView
from django.utils.translation import get_language
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.safestring import mark_safe
import json
from .calc import get_events

class CalendarTemplateView(TemplateView):
    template_name = 'events/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGE_CODE'] = get_language()
        context['get_events'] = mark_safe(json.dumps(get_events(), cls=DjangoJSONEncoder))

        return context
