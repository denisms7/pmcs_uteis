from rest_framework import generics
from datetime import date
from django.views.generic import TemplateView
from django.utils.translation import get_language
from .models import Birthday, Holidays
from . import serializers
from rest_framework.response import Response
import requests
from django.core.cache import cache

class CalendarTemplateView(TemplateView):
    template_name = 'events/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGE_CODE'] = get_language()
        return context



class CalendarListAPIView(generics.GenericAPIView):
    """
    Retorna aniversários recorrentes, feriados nacionais (BrasilAPI com cache de 1 dia)
    e feriados locais do banco.
    """

    def get(self, request, *args, **kwargs):
        today = date.today()
        years = [today.year, today.year + 1]

        events = []

        # 🎂 Aniversários
        for y in years:
            events += serializers.BirthdaySerializer(
                Birthday.objects.all(),
                many=True,
                context={"year": y}
            ).data

        # 🇧🇷 Feriados nacionais (BrasilAPI com cache de 1 dia = 86400s)
        for y in years:
            cache_key = f"feriados_brasil_{y}"
            feriados = cache.get(cache_key)

            if feriados is None:
                url = f"https://brasilapi.com.br/api/feriados/v1/{y}"
                try:
                    resp = requests.get(url, timeout=5)
                    resp.raise_for_status()
                    feriados = resp.json()
                    cache.set(cache_key, feriados, timeout=86400)  # cache por 1 dia
                except requests.RequestException:
                    feriados = []

            events += serializers.BrasilAPIFeriadoSerializer(
                feriados, many=True
            ).data

        # 🏙️ Feriados locais
        events += serializers.HolidaySerializer(
            Holidays.objects.all(), many=True
        ).data

        return Response(events)