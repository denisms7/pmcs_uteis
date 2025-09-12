from django.db import models
from django.utils import timezone


class Birthday(models.Model):
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Cadastro',
        db_index=True
    )
    name = models.CharField(max_length=150, verbose_name='Nome Completo')
    birth = models.DateField(verbose_name='Nascimento')

    class Meta:
        ordering = ["name"]
        verbose_name = "Aniversário"
        verbose_name_plural = "Aniversários"

    def __str__(self):
        return self.name


class Holidays(models.Model):
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Cadastro',
        db_index=True
    )
    name = models.CharField(max_length=150, verbose_name='Feriado')
    date = models.DateField(verbose_name='Data')

    class Meta:
        ordering = ["name"]
        verbose_name = "Feriado"
        verbose_name_plural = "Feriados"

    def __str__(self):
        return self.name
