import requests
from cities_light.models import Country
from django.core.management import BaseCommand

from src.apps.posts.utils import countries


class Command(BaseCommand):
    help = "Create regions/states for countries"

    def handle(self, *args, **options):
        api_url = "https://countriesnow.space/api/v0.1/countries/states"
        region_names = ['state', 'oblast', 'district']
        for country in countries:
            country_obj = Country.objects.get(geoname_id=country.get('geoname_id'))

            payload = {
                "country": country.get("name")
            }

            response = requests.post(api_url, json=payload)

            if response.status_code == 200:
                data = response.json()
                if data.get("error"):
                    print(f"Failed to get states for country: {country.get('name')}")
                data = response.json()

                regions = data.get("data", {}).get("states", [])
                for region in regions:
                    state_name = region.get("name")
                    if state_name and any(word in state_name.lower() for word in region_names):
                        for word in region_names:
                            state_name = state_name.lower().replace(word, "").strip().capitalize()
                    if state_name:
                        country_obj.region_set.get_or_create(name=state_name)

                print(f"States created successfully for country: {country.get('name')}")
            else:
                print("Request to api failed with status code:", response.status_code)