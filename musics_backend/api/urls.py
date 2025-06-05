# movies_backend/api/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('cards/random/', views.random_cards, name='random_cards'),
    # outras rotas do seu app "api"...
]
