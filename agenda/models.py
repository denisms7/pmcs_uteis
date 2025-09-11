from django.db import models


class Grupo(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    grupo = models.CharField(max_length=200, verbose_name='Grupo')
    numero = models.CharField(max_length=5, verbose_name='Numero')
    def __str__(self):
        return f"{self.grupo}"


class Agenda(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    grupo = models.ForeignKey(Grupo, on_delete=models.PROTECT, verbose_name='Agenda', null=True, blank=True)
    pessoa = models.CharField(max_length=200, verbose_name='Pessoa')
    numero_interno = models.CharField(max_length=20, verbose_name='Numero Interno')
    numero_externo = models.CharField(max_length=20, verbose_name='Numero Externo', null=True, blank=True)
    def __str__(self):
        return f"{self.pessoa} - {self.numero_interno}"
