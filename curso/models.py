from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')

    @property
    def video_url(self):
        return self.video_file.url