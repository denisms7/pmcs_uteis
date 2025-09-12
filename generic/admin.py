from django.contrib import admin
from .models import Category, Button, Legislation, LegislationButton


class ButtonInline(admin.TabularInline):
    model = Button
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "button_color", "text_color", "created_at")
    search_fields = ("name", "description")
    ordering = ("name",)
    inlines = [ButtonInline]


@admin.register(Button)
class ButtonAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "created_at")
    search_fields = ("title", "description", "url")
    list_filter = ("category",)
    ordering = ("title",)


@admin.register(Legislation)
class LegislationAdmin(admin.ModelAdmin):
    list_display = ("document", "category", "url", "created_at")
    search_fields = ("document", "description", "url")
    list_filter = ("category",)
    ordering = ("document",)


@admin.register(LegislationButton)
class LegislationButtonAdmin(admin.ModelAdmin):
    list_display = ("title", "url", "created_at")
    search_fields = ("title", "description", "url")
    ordering = ("title",)
