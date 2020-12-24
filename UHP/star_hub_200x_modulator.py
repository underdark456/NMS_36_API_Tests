import requests
from bs4 import BeautifulSoup


def modulator_txlvl():
    modulator_response = requests.get('http://10.0.3.150/cm3?da=1')
    soup = BeautifulSoup(modulator_response.text, 'lxml')
    values = [element['value'] for element in soup.findAll('input', {'type': 'text'})]
    return float(values[0] + '.' + values[1])
