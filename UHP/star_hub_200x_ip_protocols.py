import requests
from bs4 import BeautifulSoup


def SNMP():
    SNMP_respone = requests.get('http://10.0.3.150/cc9')
    soup = BeautifulSoup(SNMP_respone.text, 'lxml')
    values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    return values


def DHCP():
    DHCP_respone = requests.get('http://10.0.3.150/cc8')
    soup = BeautifulSoup(DHCP_respone.text, 'lxml')
    values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    mode = tuple([element['value'] for element in soup.find_all('option', selected=True)])
    return mode + values
