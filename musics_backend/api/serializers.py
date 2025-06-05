from rest_framework import serializers
from .models import Movie
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'song', 'artist', 'phrase']