from django.urls import path
from .views import random_cards

urlpatterns = [
    path('cards/random/', random_cards, name='random-cards'),
]
