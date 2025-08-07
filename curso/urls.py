from django.urls import path
from .views import video_player, Cursos, CursoAdded, CursoEdit, CursoSearch

urlpatterns = [
    path('cursos/', Cursos, name='cursos'),
    path('video/<int:video_id>/', video_player, name='video_player'),


    path('curso/busca/', CursoSearch.as_view(), name='CursoBusca'),
    path('curso/added/', CursoAdded.as_view(), name='CursoAdded'),
    path('curso/<int:pk>/update/', CursoEdit.as_view(), name='CursoEdit'),
]
