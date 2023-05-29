from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Video


class Cursos(TemplateView):
    template_name = 'curso\index.html'


def video_player(request, video_id):
    video = Video.objects.get(pk=video_id)
    return render(request, 'curso\player.html', {'video': video})
