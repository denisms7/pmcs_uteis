from django.urls import path
from .views import CalendarioView, agendamentos_json

urlpatterns = [
    path('calendario/', CalendarioView.as_view(), name='calendario'),
    path('calendario/eventos/', agendamentos_json, name='eventos_consulta_json'),
]
