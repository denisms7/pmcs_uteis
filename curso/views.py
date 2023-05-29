from django.shortcuts import render
from .models import Video

def video_player(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video_player.html', {'video': video})
