from django.urls import path
from .views import random_movie, movie_choices, random_cards

urlpatterns = [
    path('movies/random/', random_movie),
    path('movies/choices/', movie_choices),
    path('cards/random/', random_cards, name='random-cards'),
]
