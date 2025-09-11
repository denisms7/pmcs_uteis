from django.contrib import admin
from .models import Birthday, Holidays


@admin.register(Birthday)
class BirthdayAdmin(admin.ModelAdmin):
    list_display = ("name", "birth")
    list_filter = ("birth",)
    search_fields = ("name",)
    ordering = ("-name",)


@admin.register(Holidays)
class HolidaysAdmin(admin.ModelAdmin):
    list_display = ("name", "date")
    list_filter = ("date",)
    search_fields = ("name",)
    ordering = ("-name",)
