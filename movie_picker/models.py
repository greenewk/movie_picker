from django.db import models

class Movie(models.Model):
    title = models.TextField(default='')

    def __str__(self):
        return self.title

