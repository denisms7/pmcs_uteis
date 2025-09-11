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
        # sempre atualiza o ano do aniversário para o ano atual
        birthday_this_year = obj.birth.replace(year=today.year)
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
