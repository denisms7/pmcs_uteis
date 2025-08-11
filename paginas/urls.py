from django.urls import path
from .views import PaginaInicial, InteligenciaA, PDM, HinoNacional, HinoEstadual, HinoMunicipal
from .views import EnderecoOficiais, Sismel, Atalhos, Speed_test, VideoTreinamentoView

urlpatterns = [
    path('', PaginaInicial.as_view(), name='inicio'),
    path('ia/', InteligenciaA.as_view(), name='InteligenciaA'),
    path('pdm/', PDM.as_view(), name='pdm_municipal'),

    path('hino/nacional/', HinoNacional.as_view(), name='hino_nacional'),
    path('hino/estadual/', HinoEstadual.as_view(), name='hino_estadual'),
    path('hino/municipal/', HinoMunicipal.as_view(), name='hino_municipal'),
    path('enderecos-oficiais/', EnderecoOficiais.as_view(), name='enderecos_of'),
    path('atalhosdeteclado/', Atalhos.as_view(), name='atalhos-teclado'),
    path('sismel/', Sismel.as_view(), name='sismel'),
    path('SpeedTest-pmcs/', Speed_test.as_view(), name='SpeedTest'),

    path('video-treinamento/', VideoTreinamentoView.as_view(), name='video_treinamento'),
]
