from objects import ss_100x_json
from objects import cidr_to_netmask

def acceleration():
    return ss_100x_json()['data']['accel_enable'], \
           ss_100x_json()['data']['accel_svlan_from'], \
           ss_100x_json()['data']['accel_svlan_to'], \
           ss_100x_json()['data']['accel_mss'], \
           ss_100x_json()['data']['accel_max_tcp_window'], \
           ss_100x_json()['data']['accel_tcp_rcvwnd_update'], \
           ss_100x_json()['data']['accel_sessions'], \
           ss_100x_json()['data']['accel_buffers'], \
           ss_100x_json()['data']['accel_max_queue'], \
           ss_100x_json()['data']['accel_max_mod_queue'], \
           ss_100x_json()['data']['accel_retransmit_timeout'], \
           ss_100x_json()['data']['accel_retransmit_tries'], \
           ss_100x_json()['data']['accel_inactivity_timeout'], \
           ss_100x_json()['data']['accel_ack_period']

def encryption():
    '''Флаг aes v.34/v.35 работает только на прошивках 3.5'''
    return ss_100x_json()['data']['crypto_flags'], \
           ss_100x_json()['data']['crypto_key']
    #objects.star_hub_200x.star_hub_200x_json()['aes']
def dhcp():
    return ss_100x_json()['data']['dhcp_enable'], \
           ss_100x_json()['data']['dhcp_vlan'], \
           ss_100x_json()['data']['dhcp_ip_start'], \
           ss_100x_json()['data']['dhcp_ip_end'], \
           cidr_to_netmask(ss_100x_json()['data']['dhcp_mask']), \
           ss_100x_json()['data']['dhcp_gw'], \
           ss_100x_json()['data']['dhcp_dns'], \
           str(ss_100x_json()['data']['dhcp_lease'])

def dns():
    return ss_100x_json()['data']['dns_enable'], \
           ss_100x_json()['data']['dns_clear_timeout']

def ip_screening():
    return ss_100x_json()['data']['ipscreen_enable']

def snmp():
    return ss_100x_json()['data']['snmp_ip1'], \
           ss_100x_json()['data']['snmp_ip2'], \
           ss_100x_json()['data']['snmp_read'], \
           ss_100x_json()['data']['snmp_write']

def tftp():
    return ss_100x_json()['data']['tftp_ip'], \
           ss_100x_json()['data']['tftp_vlan']

def multicast():
    return ss_100x_json()['data']['multicast_mode'], \
           ss_100x_json()['data']['multicast_timeout']

def arp():
    return ss_100x_json()['data']['arp_timeout'], \
           ss_100x_json()['data']['arp_proxy_enable']

def nat():
    '''Нет Port Forwarding'''
    return ss_100x_json()['data']['nat_enable'], \
           ss_100x_json()['data']['nat_external_ip'], \
           ss_100x_json()['data']['nat_internal_network'], \
           cidr_to_netmask(ss_100x_json()['data']['nat_internal_mask'])

def rip():
    return ss_100x_json()['data']['rip_enable'], \
           ss_100x_json()['data']['rip_gateway_ip'], \
           ss_100x_json()['data']['rip_omit_down_stations'], \
           ss_100x_json()['data']['rip_couple_to_sm_alarms'], \
           ss_100x_json()['data']['rip_routes_cost']

def sntp():
    '''Нет mode'''
    return ss_100x_json()['data']['sntp_ip'], \
           ss_100x_json()['data']['sntp_vlan']

def realtime_bw():
    return ss_100x_json()['data']['realtime_bw_codec'], \
           ss_100x_json()['data']['realtime_bw_threshold'], \
           ss_100x_json()['data']['realtime_bw_timeout']
