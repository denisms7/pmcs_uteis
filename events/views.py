from rest_framework import generics
from django.views.generic import TemplateView
from django.utils.translation import get_language
from .models import Birthday, Holidays
from . import serializers
from rest_framework.response import Response


class CalendarTemplateView(TemplateView):
    template_name = 'events/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['LANGUAGE_CODE'] = get_language()
        return context


class CalendarListAPIView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        birthdays = serializers.BirthdaySerializer(Birthday.objects.all(), many=True).data
        holidays = serializers.HolidaySerializer(Holidays.objects.all(), many=True).data

        events = birthdays + holidays
        return Response(events)
