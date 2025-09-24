from django.contrib import admin
from .models import OfficialAddress, Schedule, Category


@admin.register(Category)
class OfficialAddressAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(OfficialAddress)
class OfficialAddressAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address", "operation", "created_at")
    search_fields = ("name", "address", "phone")
    ordering = ("name",)
    readonly_fields = ("created_at",)



@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("person", "person_num",)
    search_fields = ("person", "person_num", "sector", "sector_num",)
    ordering = ("person",)
    readonly_fields = ("created_at",)
    list_filter = ("address",)
