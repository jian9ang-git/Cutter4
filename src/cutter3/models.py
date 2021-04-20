from django.db import models
from django.utils import timezone
from datetime import date


class UrlShort(models.Model):
    user_url = models.URLField(max_length=2000)
    short_url = models.CharField(max_length=2000, default=None)
    num_visits = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_url

