from objects import sh_200x_json
from objects import cidr_to_netmask

from NMS_API.lists.modems import ip_prot
from NMS_API.options import values_


def acceleration():
    return values_(ip_prot.accel)

def encryption():
    '''Флаг aes v.34/v.35 работает только на прошивках 3.5'''
    return values_(ip_prot.crypto)

def dhcp():
    return sh_200x_json()['data'][ip_prot.dhcp[0]], \
           sh_200x_json()['data'][ip_prot.dhcp[1]], \
           sh_200x_json()['data'][ip_prot.dhcp[2]], \
           sh_200x_json()['data'][ip_prot.dhcp[3]], \
           cidr_to_netmask(sh_200x_json()['data'][ip_prot.dhcp[4]]), \
           sh_200x_json()['data'][ip_prot.dhcp[5]], \
           sh_200x_json()['data'][ip_prot.dhcp[6]], \
           str(sh_200x_json()['data'][ip_prot.dhcp[7]])



def dns():
    return values_(ip_prot.dns)

def ip_screening():
    return values_(ip_prot.screen)

def snmp():
    '''http://redmine.eastar.ru/issues/7364'''
    return values_(ip_prot.snmp)

def tftp():
    return values_(ip_prot.tftp)

def multicast():
    return values_(ip_prot.multicast)

def arp():
    return values_(ip_prot.arp)

def nat():
    '''Нет Port Forwarding'''
    '''Маска в другом формате'''
    return sh_200x_json()['data']['nat_enable'], \
           sh_200x_json()['data']['nat_external_ip'], \
           sh_200x_json()['data']['nat_internal_network'], \
           cidr_to_netmask(sh_200x_json()['data']['nat_internal_mask'])

def rip():
    return values_(ip_prot.rip)

def sntp():
    '''Нет mode'''
    return values_(ip_prot.sntp)

def realtime_bw():
    return values_(ip_prot.bw)

