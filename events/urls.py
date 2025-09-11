from django.urls import path
from .views import CalendarTemplateView, CalendarListAPIView

urlpatterns = [
    path('calendario/', CalendarTemplateView.as_view(), name='calendar'),
    path('calendario/api/', CalendarListAPIView.as_view(), name='calendar_api'),
]
 