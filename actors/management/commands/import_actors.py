from django.core.management import BaseCommand
import csv
from datetime import datetime
from actors.models import Actor


class Command(BaseCommand):
    help = "Comando customizado para importar atores de um arquivo CSV."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV contendo os dados dos atores.')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                birthday = datetime.strptime(row['birthday'], '%Y-%m-%d').date()
                nationality = row['nationality']

                self.stdout.write(self.style.NOTICE(f'Importando ator: {name}'))

                Actor.objects.create(
                    name=name,
                    birth_date=birthday,
                    nationality=nationality
                )
        self.stdout.write(self.style.SUCCESS('Atores importados com sucesso!'))