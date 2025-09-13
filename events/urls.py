from django.urls import path
from .views import CalendarTemplateView, CalendarListAPIView


urlpatterns = [
    path('calendario/', CalendarTemplateView.as_view(), name='calendar'),
    path('calendario/api/v1/', CalendarListAPIView.as_view(), name='calendar_api'),
]
