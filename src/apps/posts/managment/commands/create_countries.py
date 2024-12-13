from cities_light.abstract_models import CONTINENT_CHOICES
from django.core.management import BaseCommand

countries = [
    {'name': 'USA', 'continent': 'NA'},
    {'name': 'India', 'continent': 'AS'},
    {'name': 'France', 'continent': 'EU'},
    {'name': 'Germany', 'continent': 'EU'},
    {'name': 'Ukraine', 'continent': 'EU'},
]


class Command(BaseCommand):
    help = "Create countries"

    def handle(self, *args, **options):
        from cities_light.models import Country
        for country in countries:
            Country.objects.get_or_create(name=country['name'], continent=country['continent'])
        self.stdout.write(self.style.SUCCESS(f'Countries created successfully: {*[country["name"] for country in countries],}'))