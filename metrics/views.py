from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta
from .models import AnonymousVisit
from generic.models import Button, Category, LegislationButton
from curso.models import Video, Curso
from events.models import Birthday
from institutional.models import OfficialAddress, Schedule


def CountTable():
    data = {}
    # 14 = pdm, licitação, 4 botões de áudio, 8 imagens
    button = (Button.objects.count() or 0) + 14
    legislation_button = LegislationButton.objects.count() or 0
    # 3 = imagens, áudio, legislação
    category = (Category.objects.count() or 0) + 3
    curso = Curso.objects.count() or 0
    video = Video.objects.count() or 0
    birthday = Birthday.objects.count() or 0
    schedule = Schedule.objects.count() or 0
    officialAddress = OfficialAddress.objects.count() or 0
    anonymousvisit = AnonymousVisit.objects.count() or 0

    data['button'] = button + legislation_button
    data['category'] = category
    data['curso'] = curso
    data['video'] = video
    data['birthday'] = birthday
    data['schedule'] = schedule
    data['officialAddress'] = officialAddress
    data['anonymousvisit'] = anonymousvisit
    return data


class VisitsChartView(LoginRequiredMixin, TemplateView):
    template_name = "metrics/metrics.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Configura período (últimos 30 dias)
        days = 30
        today = timezone.now().date()
        start_date = today - timedelta(days=days - 1)

        # Lista de datas
        date_list = [start_date + timedelta(days=i) for i in range(days)]

        # Contagem diária de visitas únicas
        visits_per_day = []
        for date in date_list:
            count = AnonymousVisit.objects.filter(timestamp__date=date)\
                                          .values("session_key")\
                                          .distinct()\
                                          .count()
            visits_per_day.append(count)

        # Envia dados para o template
        context['dates'] = [d.strftime("%Y-%m-%d") for d in date_list]
        context['visits'] = visits_per_day
        context['button'] = CountTable()
        return context
