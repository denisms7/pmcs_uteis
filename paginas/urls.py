from django.urls import path
from .views import PaginaInicial, InteligenciaA, PDM
from .views import EnderecoOficiais, Speed_test
urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('ia/', InteligenciaA.as_view(), name='InteligenciaA'),
    path('pdm/', PDM.as_view(), name='pdm_municipal'),


    path('enderecos-oficiais/', EnderecoOficiais.as_view(), name='enderecos_of'),
    path('SpeedTest-pmcs/', Speed_test.as_view(), name='SpeedTest'),


]
