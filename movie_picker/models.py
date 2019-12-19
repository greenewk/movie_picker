from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.TextField(default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            on_delete=models.CASCADE,
                            null=True,)


    def __str__(self):
        return self.title

