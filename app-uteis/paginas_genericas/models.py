from django.db import models
from django.utils.translation import gettext_lazy as _

class Categoria(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    categoria = models.CharField(max_length=100, verbose_name=_('Categoria'))
    def __str__(self):
        return f"{self.curso}"
    

class Botoes(models.Model):
    BTN_CORES = [
        ('btn-primary', 'Primary'),
        ('btn-secondary', 'Secondary'),
        ('btn-success', 'Success'),
        ('btn-danger', 'Danger'),
        ('btn-warning', 'Warning'),
        ('btn-info', 'Info'),
        ('btn-light', 'Light'),
        ('btn-dark', 'Dark'),
        ('btn-link', 'Link'),
    ]


    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT, verbose_name=_('Categoria'))
    url = models.CharField(max_length=250, verbose_name=_('URL'))
    nome = models.CharField(max_length=100, verbose_name=_('Nome'))
    span = models.CharField(max_length=100, verbose_name=_('Span'))
    cor = models.CharField(max_length=50, choices=BTN_CORES, default='btn-primary')

    def __str__(self):
        return f"{self.nome} || {self.categoria.categoria}"

