from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import requests
from .models import Card
from .serializers import CardSerializer

OMDB_API_KEY = '9a1d2c3a'  # sua chave OMDb


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