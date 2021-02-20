from objects import sh_200x_json
from objects import cidr_to_netmask

from NMS_API.lists.modems import ip_prot

def acceleration():
    return sh_200x_json()['data'][ip_prot.accel[0]], \
           sh_200x_json()['data'][ip_prot.accel[1]], \
           sh_200x_json()['data'][ip_prot.accel[2]], \
           sh_200x_json()['data'][ip_prot.accel[3]], \
           sh_200x_json()['data'][ip_prot.accel[4]], \
           sh_200x_json()['data'][ip_prot.accel[5]], \
           sh_200x_json()['data'][ip_prot.accel[6]], \
           sh_200x_json()['data'][ip_prot.accel[7]], \
           sh_200x_json()['data'][ip_prot.accel[8]], \
           sh_200x_json()['data'][ip_prot.accel[9]], \
           sh_200x_json()['data'][ip_prot.accel[10]], \
           sh_200x_json()['data'][ip_prot.accel[11]], \
           sh_200x_json()['data'][ip_prot.accel[12]], \
           sh_200x_json()['data'][ip_prot.accel[13]], \
           sh_200x_json()['data'][ip_prot.accel[14]]


def encryption():
    '''Флаг aes v.34/v.35 работает только на прошивках 3.5'''
    return sh_200x_json()['data']['crypto_flags'], \
           sh_200x_json()['data']['crypto_key']
    #objects.star_hub_200x.star_hub_200x_json()['aes']
def dhcp():
    return sh_200x_json()['data']['dhcp_enable'], \
           sh_200x_json()['data']['dhcp_vlan'], \
           sh_200x_json()['data']['dhcp_ip_start'], \
           sh_200x_json()['data']['dhcp_ip_end'], \
           cidr_to_netmask(sh_200x_json()['data']['dhcp_mask']), \
           sh_200x_json()['data']['dhcp_gw'], \
           sh_200x_json()['data']['dhcp_dns'], \
           str(sh_200x_json()['data']['dhcp_lease'])

def dns():
    return sh_200x_json()['data']['dns_enable'], \
           sh_200x_json()['data']['dns_clear_timeout']

def ip_screening():
    return sh_200x_json()['data']['ipscreen_enable']

def snmp():
    return sh_200x_json()['data']['snmp_ip1'], \
           sh_200x_json()['data']['snmp_ip2'], \
           sh_200x_json()['data']['snmp_read'], \
           sh_200x_json()['data']['snmp_write']

def tftp():
    return sh_200x_json()['data']['tftp_ip'], \
           sh_200x_json()['data']['tftp_vlan']

def multicast():
    return sh_200x_json()['data']['multicast_mode'], \
           sh_200x_json()['data']['multicast_timeout']

def arp():
    return sh_200x_json()['data']['arp_timeout'], \
           sh_200x_json()['data']['arp_proxy_enable']

def nat():
    '''Нет Port Forwarding'''
    return sh_200x_json()['data']['nat_enable'], \
           sh_200x_json()['data']['nat_external_ip'], \
           sh_200x_json()['data']['nat_internal_network'], \
           cidr_to_netmask(sh_200x_json()['data']['nat_internal_mask'])

def rip():
    return sh_200x_json()['data']['rip_enable'], \
           sh_200x_json()['data']['rip_gateway_ip'], \
           sh_200x_json()['data']['rip_omit_down_stations'], \
           sh_200x_json()['data']['rip_couple_to_sm_alarms'], \
           sh_200x_json()['data']['rip_routes_cost']

def sntp():
    '''Нет mode'''
    return sh_200x_json()['data']['sntp_ip'], \
           sh_200x_json()['data']['sntp_vlan']

def realtime_bw():
    return sh_200x_json()['data']['realtime_bw_codec'], \
           sh_200x_json()['data']['realtime_bw_threshold'], \
           sh_200x_json()['data']['realtime_bw_timeout']

