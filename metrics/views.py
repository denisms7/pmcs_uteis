from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from datetime import timedelta
from .models import AnonymousVisit


class VisitsChartView(LoginRequiredMixin, TemplateView):
    template_name = "metrics/visits_chart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Configura período (últimos 30 dias)
        days = 30
        today = timezone.now().date()
        start_date = today - timedelta(days=days-1)

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
        return context
