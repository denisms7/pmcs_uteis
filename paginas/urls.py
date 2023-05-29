from django.urls import path
from .views import PaginaInicial, InteligenciaA, PDM, HinoNacional, HinoEstadual, HinoMunicipal

urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('/ia/', InteligenciaA.as_view(), name='InteligenciaA'),
    path('/pdm/', PDM.as_view(), name='pdm_municipal'),

    path('/hino/nacional/', HinoNacional.as_view(), name='hino_nacional'),
    path('/hino/estadual/', HinoEstadual.as_view(), name='hino_estadual'),
    path('/hino/municipal/', HinoMunicipal.as_view(), name='hino_municipal'),
]
