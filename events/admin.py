from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Birthday, Holidays


class BirthdayResource(resources.ModelResource):
    class Meta:
        model = Birthday
        fields = ("id", "name", "birth")
        export_order = ("id", "name", "birth")
        import_id_fields = ("name",)


@admin.register(Birthday)
class BirthdayAdmin(ImportExportModelAdmin):
    resource_class = BirthdayResource
    list_display = ("name", "birth")
    list_filter = ("birth",)
    search_fields = ("name",)
    ordering = ("-name",)
    readonly_fields = ("created_at",)


@admin.register(Holidays)
class HolidaysAdmin(admin.ModelAdmin):
    list_display = ("name", "date")
    list_filter = ("date",)
    search_fields = ("name",)
    ordering = ("-name",)
    readonly_fields = ("created_at",)
