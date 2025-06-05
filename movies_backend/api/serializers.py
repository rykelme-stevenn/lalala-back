from rest_framework import serializers
from .models import Movie
from .models import Card

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'song', 'artist', 'phrase']