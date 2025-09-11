from django.db import models


class Birthday(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome Completo')
    birth = models.DateField(verbose_name='Nascimento')

    class Meta:
        ordering = ["name"]
        verbose_name = "Aniversario"
        verbose_name_plural = "Aniversarios"

    def __str__(self):
        return f"{self.name}"


class Holidays(models.Model):
    name = models.CharField(max_length=150, verbose_name='Feriado')
    date = models.DateField(verbose_name='Data')

    class Meta:
        ordering = ["name"]
        verbose_name = "Feriado"
        verbose_name_plural = "Feriados"

    def __str__(self):
        return f"{self.name}"
