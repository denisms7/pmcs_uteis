from django.urls import path
from .views import PaginaInicial, InteligenciaA, PDM

urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('/int-art/', InteligenciaA.as_view(), name='InteligenciaA'),
    path('/PDM/', PDM.as_view(), name='pdm_municipal'),
]
