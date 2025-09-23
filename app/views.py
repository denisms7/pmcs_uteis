from django.utils import timezone
from datetime import date
from datetime import timedelta
from django.views.generic import TemplateView
from generic.models import Category, Button, LegislationButton
from curso.models import Video
from events.models import Birthday


def has_recent_video():
    ten_days_ago = timezone.now() - timedelta(days=10)
    # Verifica se existe algum vídeo com data maior ou igual a 10 dias atrás
    return Video.objects.filter(data__gte=ten_days_ago).exists()


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        today = date.today()
        context = super().get_context_data(**kwargs)
        context['birthday'] = Birthday.objects.filter(birth__month=today.month, birth__day=today.day)
        context['category'] = Category.objects.filter(active=True)
        context['legislation'] = LegislationButton.objects.filter(active=True)
        context['button'] = Button.objects.filter()
        context['has_recent_video'] = has_recent_video()
        return context


class IaTemplateView(TemplateView):
    template_name = 'home/ia.html'
