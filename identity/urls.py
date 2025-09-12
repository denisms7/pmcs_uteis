from django.urls import path
from . import views


urlpatterns = [
    path('hino/nacional/', views.NationalTemplateView.as_view(), name='hino_nacional'),
    path('hino/estadual/', views.StateTemplateView.as_view(), name='hino_estadual'),
    path('hino/municipal/', views.MunicipalTemplateView.as_view(), name='hino_municipal'),
    path('hino/independencia/', views.IndependenceTemplateView.as_view(), name='hino_independencia'),
]
