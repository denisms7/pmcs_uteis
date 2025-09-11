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
        birthday_this_year = obj.birth.replace(year=year)
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
    color = serializers.CharField(default="#FAE94E")

    def get_title(self, obj):
        return f"BR {obj['name']}"

    def get_start(self, obj):
        return obj["date"]  # BrasilAPI já manda no formato YYYY-MM-DD
