from django.urls import path
from .views import video_player, Cursos

urlpatterns = [
    path('/cursos/', Cursos, name='cursos'),
    path('video/<int:video_id>/', video_player, name='video_player'),
]
