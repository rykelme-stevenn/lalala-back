from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Card
from .serializers import CardSerializer
import random

# Armazenando os IDs das músicas já retornadas
used_song_ids = set()

@api_view(['GET'])
def random_cards(request):
    """
    Retorna 4 cards aleatórios (ou menos, se não houver 4 cadastrados),
    sem repetir músicas já retornadas.
    """
    # Conta todos os cards existentes
    total_cards = Card.objects.count()
    if total_cards == 0:
        return Response({"error": "Nenhum card cadastrado."}, status=status.HTTP_404_NOT_FOUND)

    # Se existirem menos de 4, retorna tudo. Senão, escolhe 4 idôs aleatórios.
    if total_cards <= 4:
        qs = Card.objects.all()
    else:
        # Seleciona 4 IDs distintos aleatoriamente, excluindo as músicas já usadas
        available_ids = list(Card.objects.values_list('id', flat=True).exclude(id__in=used_song_ids))
        
        # Se não houver músicas disponíveis, retorna todas as músicas
        if len(available_ids) < 4:
            return Response({"error": "Não há músicas suficientes disponíveis."}, status=status.HTTP_404_NOT_FOUND)
        
        random_ids = random.sample(available_ids, 4)
        qs = Card.objects.filter(id__in=random_ids)

        # Marcar as músicas selecionadas como "usadas"
        used_song_ids.update(random_ids)

    serializer = CardSerializer(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
