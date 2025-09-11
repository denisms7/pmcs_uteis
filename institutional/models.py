from django.db import models


class OfficialAddress(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    name = models.CharField(max_length=150, verbose_name='Local')
    phone = models.CharField(max_length=20, verbose_name='Contato')
    address = models.CharField(max_length=250, verbose_name='Logradouro')
    operation = models.CharField(max_length=250, verbose_name='Funcionamento')

    def __str__(self):
        return f"{self.grupo}"


class Group(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    name = models.CharField(max_length=200, verbose_name='Grupo')
    number = models.CharField(max_length=5, verbose_name='Numero')

    def __str__(self):
        return f"{self.name}"


class Schedule(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data')
    group = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        verbose_name='Grupo',
        null=True,
        blank=True
    )
    person = models.CharField(max_length=200, verbose_name='Pessoa')
    internal_number = models.CharField(max_length=20, verbose_name='Numero Interno')
    external_number = models.CharField(
        max_length=20,
        verbose_name='Numero Externo',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.person} - {self.internal_number}"
