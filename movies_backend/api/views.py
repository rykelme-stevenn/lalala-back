from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Movie
from .serializers import MovieSerializer
import random
import requests
from .models import Card
from .serializers import CardSerializer

OMDB_API_KEY = '9a1d2c3a'  # sua chave OMDb

@api_view(['GET'])
def random_movie(request):
    try:
        search_word = 'star'
        url = f'http://www.omdbapi.com/?s={search_word}&apikey={OMDB_API_KEY}'

        res = requests.get(url)
        res.raise_for_status()
        data = res.json()
        if data.get('Response') == 'False' or 'Search' not in data:
            return Response({'error': 'Nenhum filme encontrado'}, status=404)

        movies = data['Search']
        import random
        movie = random.choice(movies)

        imdb_id = movie['imdbID']
        detail_url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={OMDB_API_KEY}'
        detail_res = requests.get(detail_url)
        detail_res.raise_for_status()
        detail_data = detail_res.json()

        movie_data = {
            'id': detail_data.get('imdbID'),
            'title': detail_data.get('Title'),
            'description': detail_data.get('Plot'),
            'genre': detail_data.get('Genre'),
            'director': detail_data.get('Director'),
            'poster_url': detail_data.get('Poster'),
        }

        return Response(movie_data)

    except Exception as e:
        return Response({'error': str(e)}, status=500)

@api_view(['POST'])
def movie_choices(request):
    chosen_movies_ids = request.data.get('chosen_movies', [])
    chosen_movies = Movie.objects.filter(id__in=chosen_movies_ids)
    genres = [movie.genre for movie in chosen_movies]

    recommended = Movie.objects.filter(genre__in=genres).exclude(id__in=chosen_movies_ids)[:5]
    serializer = MovieSerializer(recommended, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def random_cards(request):
    try:
        total_cards = Card.objects.count()
        if total_cards < 4:
            return Response({'error': 'Não há cards suficientes no banco.'}, status=400)

        # Pega 4 IDs aleatórios diferentes
        random_ids = random.sample(list(Card.objects.values_list('id', flat=True)), 4)
        cards = Card.objects.filter(id__in=random_ids)

        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)