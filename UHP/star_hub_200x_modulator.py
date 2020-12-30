import requests
from bs4 import BeautifulSoup
from objects import star_hub_200x

def modulator_txlvl():
    modulator_response = requests.get(f'{star_hub_200x.star_hub_200x_url()}cm3?da=1')
    soup = BeautifulSoup(modulator_response.text, 'lxml')
    values = [element['value'] for element in soup.findAll('input', {'type': 'text'})]
    return float(values[0] + '.' + values[1])
