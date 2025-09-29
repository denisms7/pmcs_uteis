from django.db import models


class AnonymousVisit(models.Model):
    session_key = models.CharField(max_length=40)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visit {self.session_key} at {self.timestamp}"
