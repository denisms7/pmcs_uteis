from django.db import models
from django.utils.translation import gettext_lazy as _


class Grupo(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    grupo = models.CharField(max_length=200, verbose_name=_('Grupo'))
    numero = models.CharField(max_length=5, verbose_name=_('Numero'))
    def __str__(self):
        return f"{self.grupo}"


class Agenda(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name=_('Agenda'), null=True, blank=True)
    pessoa = models.CharField(max_length=200, verbose_name=_('Pessoa'))
    numero_interno = models.CharField(max_length=20, verbose_name=_('Numero Interno'))
    numero_externo = models.CharField(max_length=20, verbose_name=_('Numero Externo'), null=True, blank=True)
    def __str__(self):
        return f"{self.pessoa} - {self.numero_interno}"



