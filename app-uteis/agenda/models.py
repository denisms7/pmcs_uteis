from django.db import models
from django.utils.translation import gettext_lazy as _


class Grupo(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    grupo = models.CharField(max_length=200, verbose_name=_('Grupo'))
    def __str__(self):
        return f"{self.grupo}"


class Agenda(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name=_('Agenda'))
    pessoa = models.CharField(max_length=200, verbose_name=_('Pessoa'))
    numero = models.CharField(max_length=20, verbose_name=_('Numero'))
    def __str__(self):
        return f"{self.pessoa} - {self.numero}"



