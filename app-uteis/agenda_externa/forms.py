from django import forms
from django.core.exceptions import ValidationError
from .models import Agenda_Externa

class FormAgendaExterna(forms.ModelForm):

    class Meta:
        model = Agenda_Externa
        fields = [
            'destino',
            'ramal',
            'numero_externo',
        ]

    def clean_numero_externo(self):
        numero = self.cleaned_data.get('numero_externo')
        if len(numero) < 14 or len(numero) > 16:
            raise ValidationError('Número inválido')
        return numero


    def clean_ramal(self):
        ramal = self.cleaned_data.get('ramal')
        if ramal is not None and len(ramal) > 0:
            if not ramal.isdigit():
                raise ValidationError('O ramal deve conter apenas números')
        return ramal