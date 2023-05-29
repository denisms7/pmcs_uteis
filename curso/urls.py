from django.urls import path
from .views import video_player

urlpatterns = [
    path('video/<int:video_id>/', video_player, name='video_player'),
]
