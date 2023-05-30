from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Video, Curso
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import FormCurso


def Cursos(request):
    video = Video.objects.all()
    cursos = Curso.objects.all()
    return render(request, 'curso\index.html', {'video': video, 'cursos': cursos})


def video_player(request, video_id):
    video = Video.objects.get(pk=video_id)
    return render(request, 'curso\player.html', {'video': video})




class CursoAdded(LoginRequiredMixin, CreateView):
    form_class = FormCurso 
    template_name = 'curso/forms/index.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        messages.success(self.request, "Curso salvo com sucesso.")
        return super().form_valid(form)

class CursoEdit(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = FormCurso
    template_name = 'curso/forms/index.html'
    success_url = reverse_lazy('inicio')

    def form_valid(self, form):
        messages.success(self.request, "Curso atualizado com sucesso.")
        return super().form_valid(form)