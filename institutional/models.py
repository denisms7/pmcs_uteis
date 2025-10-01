from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Categoria', unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Endereço - Categoria"
        verbose_name_plural = "Endereços - Categorias"

    def __str__(self):
        return f"{self.name}"


class OfficialAddress(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Alterado')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Categoria')
    name = models.CharField(max_length=150, verbose_name='Local', unique=True)
    phone = models.CharField(max_length=20, verbose_name='Contato', null=True, blank=True)
    address = models.CharField(max_length=250, verbose_name='Logradouro', null=True, blank=True)
    operation = models.CharField(max_length=250, verbose_name='Funcionamento', null=True, blank=True)
    maps = models.URLField(max_length=250, verbose_name='Maps', null=True, blank=True)

    class Meta:
        ordering = ["category", "name"]
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

    def __str__(self):
        return f"{self.name}"


class Schedule(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastro')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Alterado')
    person = models.CharField(max_length=150, verbose_name='Pessoa', unique=True)
    person_num = models.CharField(max_length=10, verbose_name='Pessoa Numero')
    sector = models.CharField(max_length=150, verbose_name='Setor', null=True, blank=True)
    sector_num = models.CharField(max_length=10, verbose_name='Setor Numero', null=True, blank=True)
    address = models.ForeignKey(OfficialAddress, on_delete=models.PROTECT, verbose_name='Endereço', null=True, blank=True)

    class Meta:
        ordering = ["address", "person"]
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"

    def __str__(self):
        return f"{self.person} - {self.person_num}"
