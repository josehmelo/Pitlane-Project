import requests

BASE_URL = "http://api.jolpi.ca/ergast/f1"

def get_construtores(ano):
    url = f"{BASE_URL}/{ano}/constructors.json?limit=100"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data['MRData']['ConstructorTable']['Constructors']

def get_pilotos(ano):
    url = f"{BASE_URL}/{ano}/drivers.json?limit=100"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data['MRData']['DriverTable']['Drivers']

def get_pilotos_qualificacao(ano):
    url = f"{BASE_URL}/{ano}/driverStandings.json?limit=1000"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    qualificacao = data['MRData']['StandingsTable']['StandingsLists']
    if qualificacao:
        return qualificacao[0]['DriverStandings']
    return []

def construtor_qualificacao(ano):
    url = f"{BASE_URL}/{ano}/constructorStandings.json?limit=1000"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    qualificacao = data['MRData']['StandingsTable']['StandingsLists']
    if qualificacao:
        return qualificacao[0]['ConstructorStandings']
    return []