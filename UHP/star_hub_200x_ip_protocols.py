import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

sh_200x_url = 'http://10.0.3.152/'

'''По поводу галочек...Тэг checked появляется только когда галка enable on.'''
def SNMP():
    SNMP_respone = requests.get(f'{sh_200x_url}cc9')
    soup = BeautifulSoup(SNMP_respone.text, 'lxml')
    values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    return values

def DHCP():
    DHCP_respone = requests.get(f'{sh_200x_url}cc8')
    soup = BeautifulSoup(DHCP_respone.text, 'lxml')
    values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    mode = tuple([element['value'] for element in soup.find_all('option', selected=True)])
    return mode + values

def DNS():
    DNS_respone = requests.get(f'{sh_200x_url}cc59')
    soup = BeautifulSoup(DNS_respone.text, 'lxml')
    values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    values = str(values[0])
    print(values)
    mode = soup.find_all('input', checked=True)
    mode = str(mode)
    if "1" not in mode:
        return ("0",) + (values,)
    else:
        return ("0",) + (values,)

def ARP():
    ARP_respone = requests.get(f'{sh_200x_url}cc23')
    soup = BeautifulSoup(ARP_respone.text, 'lxml')
    values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    values = str(values[0])
    print(values)
    mode = soup.find_all('input', checked=True)
    mode = str(mode)
    if "1" not in mode:
        return (values,) + ("0",)
    else:
        return (values,) + ("0",)

def NAT():
    NAT_respone = requests.get(f'{sh_200x_url}cc7')
    soup = BeautifulSoup(NAT_respone.text, 'lxml')
    values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    mode = soup.find_all('input', checked=True)
    mode = str(mode)
    if "1" not in mode:
        return ("0",) + (values)
    else:
        return ("0",) + (values)

