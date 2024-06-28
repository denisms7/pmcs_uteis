from django.urls import path
from .views import v_AgendaExterna, AgendaExternaCreateView

urlpatterns = [
    path('agenda/externa/', v_AgendaExterna.as_view(), name='Agenda_Externa'),
    path('agenda/externa/added/', AgendaExternaCreateView.as_view(), name='Agenda_Externa_added')
]
