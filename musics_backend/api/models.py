from django.db import models

# Create your models here.
from django.db import models

class Card(models.Model):
    song = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    phrase = models.TextField()

    def __str__(self):
        return f"{self.song} - {self.artist}"