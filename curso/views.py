from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Video, Curso



def Cursos(request):
    video = Video.objects.all()
    cursos = Curso.objects.all()
    return render(request, 'curso\index.html', {'video': video, 'cursos': cursos})


def video_player(request, video_id):
    video = Video.objects.get(pk=video_id)
    return render(request, 'curso\player.html', {'video': video})
