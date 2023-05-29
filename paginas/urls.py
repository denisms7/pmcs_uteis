from django.urls import path
from .views import PaginaInicial, InteligenciaA

urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('/int-art/', InteligenciaA.as_view(), name='InteligenciaA'),
]
