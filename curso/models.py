from django.db import models
from django.utils.translation import gettext_lazy as _


class Curso(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    curso = models.CharField(max_length=200, verbose_name=_('Nome do Curso'))
    cor_botao = models.CharField(max_length=10, verbose_name=_('Cor Botões'), default="#0B5ED7")
    cor_texto = models.CharField(max_length=10, verbose_name=_('Cor Textos'), default="#fff")
    descricao = models.TextField(max_length=2000, verbose_name=_('Descrição'), null=True, blank=True)
    def __str__(self):
        return f"{self.curso}"


class Video(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name=_('Curso'))
    title = models.CharField(max_length=100, verbose_name=_('Título'))
    descricao = models.TextField(max_length=2000, verbose_name=_('Descrição'), null=True, blank=True)
    video_file = models.FileField(upload_to='videos/', verbose_name=_('Vídeo'))
    
    @property
    def video_url(self):
        return self.video_file.url
    
    def __str__(self):
        return f"{self.curso.curso} || {self.title}"
