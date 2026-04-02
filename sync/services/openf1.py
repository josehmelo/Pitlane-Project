import requests

BASE_URL = "https://api.openf1.org/v1"

def get_pilotos(ano):
    url = f"{BASE_URL}/pilotos?season={ano}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()