# movies_backend/api/views.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Card
from .serializers import CardSerializer
import random

@api_view(['GET'])
def random_cards(request):
    print("entrou aqui")
    """
    Retorna 4 cards aleatórios (ou menos, se não houver 4 cadastrados).
    """
    # Conta todos os cards existentes
    total_cards = Card.objects.count()
    if total_cards == 0:
        return Response({"error": "Nenhum card cadastrado."}, status=status.HTTP_404_NOT_FOUND)

    # Se existirem menos de 4, retorna tudo. Senão, escolhe 4 idôs aleatórios.
    if total_cards <= 4:
        qs = Card.objects.all()
    else:
        # Seleciona 4 IDs distintos aleatoriamente
        ids = list(Card.objects.values_list('id', flat=True))
        random_ids = random.sample(ids, 4)
        qs = Card.objects.filter(id__in=random_ids)

    serializer = CardSerializer(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
