import requests
from bs4 import BeautifulSoup
'''По поводу галочек...Тэг checked появляется только когда галка enable on.
   Чекбоксы находятся по соответствующему name'''

def SNMP(url):
    SNMP_respone = requests.get(f'{url}cc9')
    soup = BeautifulSoup(SNMP_respone.text, 'lxml')
    SNMP_values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    return SNMP_values

def DHCP(url):
    DHCP_respone = requests.get(f'{url}cc8')
    soup = BeautifulSoup(DHCP_respone.text, 'lxml')
    DHCP_values = [element['value'] for element in soup.findAll('input', {'type': 'text'})]
    mode = soup.find('option', selected=True)['value']
    return (mode,) + (*DHCP_values,)

def DNS(url):
    DNS_respone = requests.get(f'{url}cc59')
    soup = BeautifulSoup(DNS_respone.text, 'lxml')
    Clear_timeout = soup.find('input', attrs={'name': 'db'})['value']
    mode = str(soup.find_all('input', checked=True))
    if "1" not in mode:
        return ("0",) + (Clear_timeout,)
    else:
        return ("1",) + (Clear_timeout,)

def ARP(url):
    ARP_respone = requests.get(f'{url}cc23')
    soup = BeautifulSoup(ARP_respone.text, 'lxml')
    Arp_table_clear = soup.find('input', attrs={'name': 'da'})['value']
    mode = str(soup.find_all('input', checked=True))
    if "1" not in mode:
        return (Arp_table_clear,) + ("0",)
    else:
        return (Arp_table_clear,) + ("1",)

def NAT(url):
    '''не реализован порт форвард в апи нмса'''
    NAT_respone = requests.get(f'{url}cc7')
    soup = BeautifulSoup(NAT_respone.text, 'lxml')
    External_IP = soup.find('input', attrs={'name': 'if'})['value']
    Internal_network = soup.find('input', attrs={'name': 'ih'})['value']
    Internal_mask = soup.find('input', attrs={'name': 'mg'})['value']
    # External_port = soup.findAll("td")[9].text
    # Internal_IP = soup.findAll("td")[10].text
    # Internal_port = soup.findAll("td")[11].text
    mode = str(soup.find_all('input', checked=True))
    if "1" not in mode:
         return ("0",) + (External_IP,Internal_network,Internal_mask)
    else:
         return ("1",) + (External_IP,Internal_network,Internal_mask)

def RIP(url):
    RIP_respone = requests.get(f'{url}cc10')
    soup = BeautifulSoup(RIP_respone.text, 'lxml')
    Gateway_IP = soup.find('input', attrs={'name': 'ia'})['value']
    Routes_cost = soup.find('input', attrs={'name': 'de'})['value']
    mode = str(soup.find('input',attrs={'name': 'db'}, checked=True))
    if "1" not in mode:
        part1 = ("0",Gateway_IP)
    else:
        part1 = ("1",Gateway_IP)
    Omit_down_stations = str(soup.find('input',attrs={'name': 'dc'}, checked=True))
    if "1" not in Omit_down_stations:
        part2 = (*part1,) + ("0",)
    else:
        part2 = (*part1,) + ("1",)
    Couple_to_SM_alarms = str(soup.find('input',attrs={'name': 'dd'}, checked=True))
    if "1" not in Couple_to_SM_alarms:
        return (*part2,"0",Routes_cost)
    else:
        return (*part2,"1",Routes_cost)

def SNTP(url):
    '''В апи нмс не реализован mode'''
    SNTP_respone = requests.get(f'{url}cc11')
    soup = BeautifulSoup(SNTP_respone.text, 'lxml')
    Server_IP = soup.find('input', attrs={'name': 'ia'})['value']
    VLAN = soup.find('input', attrs={'name': 'dc'})['value']
    # mode = soup.find('option', selected=True)['value']
    return (Server_IP,VLAN,)

def TFTP(url):
    TFTP_respone = requests.get(f'{url}cc21')
    soup = BeautifulSoup(TFTP_respone.text, 'lxml')
    Server_IP = soup.find('input', attrs={'name': 'ia'})['value']
    VLAN = soup.find('input', attrs={'name': 'db'})['value']
    return (Server_IP,VLAN)

def Multicast(url):
    Multicast_respone = requests.get(f'{url}cc39')
    soup = BeautifulSoup(Multicast_respone.text, 'lxml')
    Multicast_timeout = soup.find('input', attrs={'name': 'da'})['value']
    mode = soup.find('option', selected=True)['value']
    return (mode,Multicast_timeout)

def Acceleration_controller(url):
    Acceleration_respone = requests.get(f'{url}cc12')
    soup = BeautifulSoup(Acceleration_respone.text, 'lxml')
    version = soup.find('option', selected=True)['value']
    values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    mode = str(soup.find('input', attrs={'name': 'da'}, checked=True))
    if "1" not in mode:
        return ("0",version,*values)
    else:
        return ("1",version,*values)

def Acceleration_station(url):
    Acceleration_respone = requests.get(f'{url}cc12')
    soup = BeautifulSoup(Acceleration_respone.text, 'lxml')
    values = tuple([element['value'] for element in soup.findAll('input', {'type': 'text'})])
    mode = str(soup.find('input', attrs={'name': 'da'}, checked=True))
    if "1" not in mode:
        return ("0", *values)
    else:
        return ("1", *values)

def IP_screening(url):
    IP_screening_respone = requests.get(f'{url}cc13')
    soup = BeautifulSoup(IP_screening_respone.text, 'lxml')
    mode = soup.find('option', selected=True)['value']
    return mode

