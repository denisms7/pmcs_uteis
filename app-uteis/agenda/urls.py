from django.urls import path
from .views import v_Agenda

urlpatterns = [
    path('agenda/', v_Agenda.as_view(), name='Agenda'),
]
