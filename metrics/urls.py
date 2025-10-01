from django.urls import path
from .views import VisitsChartView

urlpatterns = [
    path("metricas/", VisitsChartView.as_view(), name="metrics_"),
]
