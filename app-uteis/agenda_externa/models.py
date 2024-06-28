from django.db import models
from django.utils.translation import gettext_lazy as _


class Agenda_Externa(models.Model):
    data = models.DateTimeField(auto_now_add=True, verbose_name=_('Data'))
    destino = models.CharField(max_length=200, verbose_name=_('Destino'))
    ramal = models.CharField(max_length=20, verbose_name=_('Ramal (Se houver)'), blank=True)
    numero_externo = models.CharField(max_length=20, verbose_name=_(
        'Numero Externo'), null=True, blank=True)

    def __str__(self):
        return f"{self.pessoa} - {self.numero_interno}"
