# movies_backend/api/serializers.py

from rest_framework import serializers
from .models import Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'song', 'artist', 'phrase']
        