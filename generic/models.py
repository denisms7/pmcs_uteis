from django.db import models
from django.utils.translation import gettext_lazy as _

ACTIVE_CHOICES = [
    (True, _('Ativo')),
    (False, _('Inativo')),
]

class Category(models.Model):
    active = models.BooleanField(choices=ACTIVE_CHOICES, verbose_name=_('Ativo'), default=True,)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastro', db_index=True)
    name = models.CharField(max_length=200, verbose_name=_('Categoria'))
    button_color = models.CharField(max_length=10, verbose_name=_('Cor Botões'), default="#0B5ED7")
    text_color = models.CharField(max_length=10, verbose_name=_('Cor Textos'), default="#ffffff")
    description = models.TextField(max_length=2000, verbose_name=_('Descrição'), null=True, blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return f"{self.name}"


class Button(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastro', db_index=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Categoria'))
    title = models.CharField(max_length=100, verbose_name=_('Título'))
    description = models.TextField(max_length=2000, verbose_name=_('Descrição'), null=True, blank=True)
    file = models.FileField(upload_to='file/', verbose_name=_('Arquivo'), null=True, blank=True)
    url = models.URLField(max_length=250, verbose_name=_('URL'), null=True, blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Botão"
        verbose_name_plural = "Botões"

    def __str__(self):
        return f"{self.category.name} || {self.title}"


class Legislation(models.Model):

    CATEGORY_CHOICES = [
        (1, _('PDM')),
        (2, _('Licitação')),
    ]

    active = models.BooleanField(choices=ACTIVE_CHOICES, verbose_name=_('Ativo'), default=True,)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastro', db_index=True)
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, verbose_name=_('Categoria'))
    document = models.CharField(max_length=100, verbose_name=_('Documento'))
    description = models.TextField(max_length=1000, verbose_name=_('Descrição'))
    file = models.FileField(upload_to='file/', verbose_name=_('Arquivo'), null=True, blank=True)
    url = models.URLField(max_length=250, verbose_name=_('URL'), null=True, blank=True)

    class Meta:
        ordering = ["document"]
        verbose_name = "Licitação/PDM"
        verbose_name_plural = "Licitações/PDM"

    def __str__(self):
        return f"{self.category} || {self.document}"


class LegislationButton(models.Model):
    active = models.BooleanField(choices=ACTIVE_CHOICES, verbose_name=_('Ativo'), default=True,)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cadastro', db_index=True)
    title = models.CharField(max_length=100, verbose_name=_('Título'))
    description = models.TextField(max_length=2000, verbose_name=_('Descrição'), null=True, blank=True)
    file = models.FileField(upload_to='file/', verbose_name=_('Arquivo'), null=True, blank=True)
    url = models.URLField(max_length=250, verbose_name=_('URL'), null=True, blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Botão Legislação"
        verbose_name_plural = "Botão Legislação"

    def __str__(self):
        return f"Legislação || {self.title}"