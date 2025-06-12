from django.core.cache import cache
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Card
import random
from .serializers import CardSerializer

@api_view(['GET'])
def random_cards(request):
    """
    Retorna 4 cards aleatórios sem repetir músicas durante a sessão.
    As músicas já selecionadas são armazenadas em cache.
    """
    # Tenta recuperar o cache de IDs de músicas já usadas
    used_song_ids = cache.get('used_song_ids', [])
    
    # Conta todos os cards existentes
    total_cards = Card.objects.count()
    if total_cards == 0:
        return Response({"error": "Nenhum card cadastrado."}, status=status.HTTP_404_NOT_FOUND)

    # Se existirem menos de 4 músicas, retorna tudo
    if total_cards <= 4:
        qs = Card.objects.all()
    else:
        # Seleciona 4 IDs distintos aleatoriamente
        ids = list(Card.objects.values_list('id', flat=True))
        available_ids = [id for id in ids if id not in used_song_ids]

        if len(available_ids) < 4:
            return Response({"error": "Não há músicas suficientes para selecionar 4 diferentes."}, status=status.HTTP_404_NOT_FOUND)

        random_ids = random.sample(available_ids, 4)
        qs = Card.objects.filter(id__in=random_ids)

        # Atualiza o cache com os novos IDs selecionados
        used_song_ids.extend(random_ids)
        cache.set('used_song_ids', used_song_ids, timeout=3600)  # Exemplo de timeout de 1 hora

    serializer = CardSerializer(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
