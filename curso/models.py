from django.db import models

class VideoExcel(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/excel/')
    
    @property
    def video_url(self):
        return self.video_file.url
    
    def __str__(self):
        return f"{self.title}"
