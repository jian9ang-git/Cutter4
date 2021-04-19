from django.db import models
from django.utils import timezone


class UrlShort(models.Model):
    user_url = models.URLField(max_length=2000)
    short_url = models.CharField(max_length=2000, default=None)

    def __str__(self):
        return self.user_url
