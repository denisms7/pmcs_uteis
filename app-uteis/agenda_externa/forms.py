
from django import forms
from .models import Agenda_Externa

class FormAgendaExterna(forms.ModelForm):

    class Meta:
        model = Agenda_Externa
        fields = [
            'destino',
            'ramal',
            'numero_externo',
        ]


