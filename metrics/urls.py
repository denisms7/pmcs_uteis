from django.urls import path
from .views import VisitsChartView

urlpatterns = [
    path("visitas.diarias/", VisitsChartView.as_view(), name="visits_chart"),
]
