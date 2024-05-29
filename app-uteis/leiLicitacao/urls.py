from django.urls import path
from .views import LicitacaoAjuda

urlpatterns = [
    path('licitacao/', LicitacaoAjuda.as_view(), name='licitacao_ajuda'),
]
