import objects
from NMS_API.lists.modems import ip_prot

def acceleration():
    return objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[0]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[1]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[2]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[3]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[4]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[5]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[6]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[7]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[8]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[9]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[10]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[11]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[12]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[13]], \
           objects.sh_200x.sh_200x_json()['data'][ip_prot.accel[14]]


def encryption():
    '''Флаг aes v.34/v.35 работает только на прошивках 3.5'''
    return objects.sh_200x.sh_200x_json()['data']['crypto_flags'], \
           objects.sh_200x.sh_200x_json()['data']['crypto_key']
    #objects.star_hub_200x.star_hub_200x_json()['aes']
def dhcp():
    return objects.sh_200x.sh_200x_json()['data']['dhcp_enable'], \
           objects.sh_200x.sh_200x_json()['data']['dhcp_vlan'], \
           objects.sh_200x.sh_200x_json()['data']['dhcp_ip_start'], \
           objects.sh_200x.sh_200x_json()['data']['dhcp_ip_end'], \
           objects.cidr_to_netmask(objects.sh_200x.sh_200x_json()['data']['dhcp_mask']), \
           objects.sh_200x.sh_200x_json()['data']['dhcp_gw'], \
           objects.sh_200x.sh_200x_json()['data']['dhcp_dns'], \
           str(objects.sh_200x.sh_200x_json()['data']['dhcp_lease'])

def dns():
    return objects.sh_200x.sh_200x_json()['data']['dns_enable'], \
           objects.sh_200x.sh_200x_json()['data']['dns_clear_timeout']

def ip_screening():
    return objects.sh_200x.sh_200x_json()['data']['ipscreen_enable']

def snmp():
    return objects.sh_200x.sh_200x_json()['data']['snmp_ip1'], \
           objects.sh_200x.sh_200x_json()['data']['snmp_ip2'], \
           objects.sh_200x.sh_200x_json()['data']['snmp_read'], \
           objects.sh_200x.sh_200x_json()['data']['snmp_write']

def tftp():
    return objects.sh_200x.sh_200x_json()['data']['tftp_ip'], \
           objects.sh_200x.sh_200x_json()['data']['tftp_vlan']

def multicast():
    return objects.sh_200x.sh_200x_json()['data']['multicast_mode'], \
           objects.sh_200x.sh_200x_json()['data']['multicast_timeout']

def arp():
    return objects.sh_200x.sh_200x_json()['data']['arp_timeout'], \
           objects.sh_200x.sh_200x_json()['data']['arp_proxy_enable']

def nat():
    '''Нет Port Forwarding'''
    return objects.sh_200x.sh_200x_json()['data']['nat_enable'], \
           objects.sh_200x.sh_200x_json()['data']['nat_external_ip'], \
           objects.sh_200x.sh_200x_json()['data']['nat_internal_network'], \
           objects.cidr_to_netmask(objects.sh_200x.sh_200x_json()['data']['nat_internal_mask'])

def rip():
    return objects.sh_200x.sh_200x_json()['data']['rip_enable'], \
           objects.sh_200x.sh_200x_json()['data']['rip_gateway_ip'], \
           objects.sh_200x.sh_200x_json()['data']['rip_omit_down_stations'], \
           objects.sh_200x.sh_200x_json()['data']['rip_couple_to_sm_alarms'], \
           objects.sh_200x.sh_200x_json()['data']['rip_routes_cost']

def sntp():
    '''Нет mode'''
    return objects.sh_200x.sh_200x_json()['data']['sntp_ip'], \
           objects.sh_200x.sh_200x_json()['data']['sntp_vlan']

def realtime_bw():
    return objects.sh_200x.sh_200x_json()['data']['realtime_bw_codec'], \
           objects.sh_200x.sh_200x_json()['data']['realtime_bw_threshold'], \
           objects.sh_200x.sh_200x_json()['data']['realtime_bw_timeout']

