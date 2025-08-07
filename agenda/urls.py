from django.urls import path
from .views import v_Agenda, v_Exporta

urlpatterns = [
    path('agenda/', v_Agenda.as_view(), name='Agenda'),
    path('agenda/exportacao', v_Exporta.as_view(), name='AgendaExporta'),
]
