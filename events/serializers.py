from rest_framework import serializers
from datetime import date
from .models import Birthday, Holidays


class BirthdaySerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()
    allDay = serializers.BooleanField(default=True)
    color = serializers.CharField(default="#0d6efd")

    class Meta:
        model = Birthday
        fields = ["title", "start", "allDay", "color"]

    def get_title(self, obj):
        return f"🎂 {obj.name}"

    def get_start(self, obj):
        today = date.today()
        year = self.context.get("year", today.year)

        try:
            birthday_this_year = obj.birth.replace(year=year)
        except ValueError:
            # Trata aniversários em 29/02 em anos não bissextos
            birthday_this_year = date(year, 2, 28)  # ou date(year, 3, 1) se preferir

        return birthday_this_year.isoformat()


class HolidaySerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    start = serializers.DateField(source="date")
    allDay = serializers.BooleanField(default=True)
    color = serializers.CharField(default="#dc3545")

    class Meta:
        model = Holidays
        fields = ["title", "start", "allDay", "color"]

    def get_title(self, obj):
        return f"📅 {obj.name}"


class BrasilAPIFeriadoSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    start = serializers.SerializerMethodField()  # corrigido para pegar `date`
    allDay = serializers.BooleanField(default=True)
    color = serializers.CharField(default="#000000")

    def get_title(self, obj):
        return f"📅 {obj['name']}"

    def get_start(self, obj):
        return obj["date"]  # BrasilAPI já manda no formato YYYY-MM-DD
