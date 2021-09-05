"""Core validators."""

# 3rd-party
import requests
from rest_framework.exceptions import ValidationError


def check_if_vehicle_exist(obj):  # noqa: D103
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{obj["make"]}?format=json'
    response = (requests.get(url)).json()
    if not any(m.get('Model_Name', None) == obj['model'] for m in response['Results']):
        raise ValidationError(f'Car {obj["make"]} {obj["model"]} does\'t exist')
