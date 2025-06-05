from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100, blank=True)
    poster_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Card(models.Model):
    song = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    phrase = models.TextField()

    def __str__(self):
        return f"{self.song} - {self.artist}"