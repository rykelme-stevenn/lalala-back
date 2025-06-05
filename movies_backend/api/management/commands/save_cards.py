import os
import json
from django.core.management.base import BaseCommand
from movies_backend.api.models import Card

class Command(BaseCommand):
    help = 'Importa cards do arquivo JSON'

    def handle(self, *args, **kwargs):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        path = os.path.join(BASE_DIR, 'data', 'musics.json')

        with open(path, encoding='utf-8') as f:
            data = json.load(f)

        for item in data:
          Card.objects.create(
                song=item['song'],
                artist=item['artist'],
                phrase=item['phrase'],
            )

        self.stdout.write(self.style.SUCCESS('Cards importados com sucesso!'))
