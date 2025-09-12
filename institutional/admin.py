from django.contrib import admin
from .models import OfficialAddress, Group, Schedule


@admin.register(OfficialAddress)
class OfficialAddressAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address", "operation", "created_at")
    search_fields = ("name", "address", "phone")
    list_filter = ("created_at",)
    ordering = ("name",)
    readonly_fields = ("created_at",)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "created_at")
    search_fields = ("name", "number")
    ordering = ("name",)
    readonly_fields = ("created_at",)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("person", "internal_number", "external_number", "group", "created_at")
    search_fields = ("person", "internal_number", "external_number")
    list_filter = ("group", "created_at")
    ordering = ("person",)
    readonly_fields = ("created_at",)
