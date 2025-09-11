from django.urls import path
from .views import CalendarTemplateView

urlpatterns = [
    path('calendario/', CalendarTemplateView.as_view(), name='calendar'),
]
