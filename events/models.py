from django.db import models


class Birthday(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nome Completo')
    birth = models.DateTimeField(auto_now_add=True, verbose_name='Nascimento')

    def __str__(self):
        return f"{self.name}"


class Holidays(models.Model):
    name = models.CharField(max_length=150, verbose_name='Feriado')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Data')

    def __str__(self):
        return f"{self.name}"
