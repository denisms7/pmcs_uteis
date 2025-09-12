from django import forms
from .models import Curso


class FormCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'curso',
            'cor_botao',
            'cor_texto',
            'descricao',
        ]
