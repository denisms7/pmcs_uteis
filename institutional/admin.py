from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import OfficialAddress, Schedule, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(OfficialAddress)
class OfficialAddressAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "address", "operation", "created_at")
    search_fields = ("name", "address", "phone")
    ordering = ("name",)
    list_filter = ("category",)
    readonly_fields = ('created_at', 'updated_at')


class ScheduleResource(resources.ModelResource):
    class Meta:
        model = Schedule
        fields = ("person", "person_num", "sector", "sector_num",)
        import_id_fields = ("person",)


@admin.register(Schedule)
class ScheduleAdmin(ImportExportModelAdmin):
    resource_class = ScheduleResource
    list_display = ("person", "person_num", "sector",)
    search_fields = ("person", "person_num", "sector", "sector_num",)
    ordering = ("address", "person",)
    list_filter = ("address__category", "address")
    readonly_fields = ('created_at', 'updated_at')
