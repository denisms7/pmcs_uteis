from django.contrib import admin
from .models import Video, Curso


class CursoAdmin(admin.ModelAdmin):
    list_display = ("curso", "descricao")


class VideoAdmin(admin.ModelAdmin):
    list_display = ("curso", "title", "descricao")
    list_filter = ("curso",)


admin.site.register(Video, VideoAdmin)
admin.site.register(Curso, CursoAdmin)
