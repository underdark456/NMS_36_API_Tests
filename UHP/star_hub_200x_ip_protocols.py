import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


sh_200x_url = 'http://10.0.3.152/'

'''По поводу галочек...Тэг checked появляется только когда галка enable on.'''
def SNMP():
    SNMP_respone = requests.get(f'{sh_200x_url}cc9')
    soup = BeautifulSoup(SNMP_respone.text, 'lxml')
    SNMP_values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    return SNMP_values

def DHCP():
    DHCP_respone = requests.get(f'{sh_200x_url}cc8')
    soup = BeautifulSoup(DHCP_respone.text, 'lxml')
    DHCP_values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    mode = tuple([element['value'] for element in soup.find_all('option', selected=True)])
    return mode + DHCP_values

def DNS():
    DNS_respone = requests.get(f'{sh_200x_url}cc59')
    soup = BeautifulSoup(DNS_respone.text, 'lxml')
    DNS_values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    DNS_values = str(DNS_values[0])
    mode = soup.find_all('input', checked=True)
    mode = str(mode)
    if "1" not in mode:
        return ("0",) + (DNS_values,)
    else:
        return ("0",) + (DNS_values,)

def ARP():
    ARP_respone = requests.get(f'{sh_200x_url}cc23')
    soup = BeautifulSoup(ARP_respone.text, 'lxml')
    Arp_table_clear = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    Arp_table_clear = str(Arp_table_clear[0])
    mode = soup.find_all('input', checked=True)
    mode = str(mode)
    if "1" not in mode:
        return (Arp_table_clear,) + ("0",)
    else:
        return (Arp_table_clear,) + ("0",)

def NAT():
    NAT_respone = requests.get(f'{sh_200x_url}cc7')
    soup = BeautifulSoup(NAT_respone.text, 'lxml')
    External_IP = soup.find('input', attrs={'name': 'if'})['value']
    Internal_network = soup.find('input', attrs={'name': 'ih'})['value']
    Internal_mask = soup.find('input', attrs={'name': 'mg'})['value']
    External_port = soup.findAll("td")[9].text
    Internal_IP = soup.findAll("td")[10].text
    Internal_port = soup.findAll("td")[11].text
    mode = soup.find_all('input', checked=True)
    mode = str(mode)
    if "1" not in mode:
         return ("0",) + (External_IP,Internal_network,Internal_mask,External_port,Internal_IP,Internal_port)
    else:
         return ("1",) + (External_IP,Internal_network,Internal_mask,External_port,Internal_IP,Internal_port)

