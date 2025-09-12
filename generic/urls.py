from django.urls import path
from .views import LegislationListView


urlpatterns = [
    path("legislation/<int:type>/", LegislationListView.as_view(), name="legislation_list"),
]
