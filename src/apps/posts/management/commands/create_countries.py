from cities_light.models import Country
from django.core.management import BaseCommand

from src.apps.posts.utils import countries


class Command(BaseCommand):
    help = "Create countries"

    def handle(self, *args, **options):
        for country in countries:
            Country.objects.get_or_create(name=country['name'], continent=country['continent'], geoname_id=country['geoname_id'])
            print(f'Successfully created country: {country['name']}')
