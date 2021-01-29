import objects

def acceleration():
    return objects.ss_100x.ss_100x_json()['data']['accel_enable'], \
           objects.ss_100x.ss_100x_json()['data']['accel_svlan_from'], \
           objects.ss_100x.ss_100x_json()['data']['accel_svlan_to'], \
           objects.ss_100x.ss_100x_json()['data']['accel_mss'], \
           objects.ss_100x.ss_100x_json()['data']['accel_max_tcp_window'], \
           objects.ss_100x.ss_100x_json()['data']['accel_tcp_rcvwnd_update'], \
           objects.ss_100x.ss_100x_json()['data']['accel_sessions'], \
           objects.ss_100x.ss_100x_json()['data']['accel_buffers'], \
           objects.ss_100x.ss_100x_json()['data']['accel_max_queue'], \
           objects.ss_100x.ss_100x_json()['data']['accel_max_mod_queue'], \
           objects.ss_100x.ss_100x_json()['data']['accel_retransmit_timeout'], \
           objects.ss_100x.ss_100x_json()['data']['accel_retransmit_tries'], \
           objects.ss_100x.ss_100x_json()['data']['accel_inactivity_timeout'], \
           objects.ss_100x.ss_100x_json()['data']['accel_ack_period']

def encryption():
    '''Флаг aes v.34/v.35 работает только на прошивках 3.5'''
    return objects.ss_100x.ss_100x_json()['data']['crypto_flags'], \
           objects.ss_100x.ss_100x_json()['data']['crypto_key']
    #objects.star_hub_200x.star_hub_200x_json()['aes']
def dhcp():
    return objects.ss_100x.ss_100x_json()['data']['dhcp_enable'], \
           objects.ss_100x.ss_100x_json()['data']['dhcp_vlan'], \
           objects.ss_100x.ss_100x_json()['data']['dhcp_ip_start'], \
           objects.ss_100x.ss_100x_json()['data']['dhcp_ip_end'], \
           objects.cidr_to_netmask(objects.ss_100x.ss_100x_json()['data']['dhcp_mask']), \
           objects.ss_100x.ss_100x_json()['data']['dhcp_gw'], \
           objects.ss_100x.ss_100x_json()['data']['dhcp_dns'], \
           str(objects.ss_100x.ss_100x_json()['data']['dhcp_lease'])

def dns():
    return objects.ss_100x.ss_100x_json()['data']['dns_enable'], \
           objects.ss_100x.ss_100x_json()['data']['dns_clear_timeout']

def ip_screening():
    return objects.ss_100x.ss_100x_json()['data']['ipscreen_enable']

def snmp():
    return objects.ss_100x.ss_100x_json()['data']['snmp_ip1'], \
           objects.ss_100x.ss_100x_json()['data']['snmp_ip2'], \
           objects.ss_100x.ss_100x_json()['data']['snmp_read'], \
           objects.ss_100x.ss_100x_json()['data']['snmp_write']

def tftp():
    return objects.ss_100x.ss_100x_json()['data']['tftp_ip'], \
           objects.ss_100x.ss_100x_json()['data']['tftp_vlan']

def multicast():
    return objects.ss_100x.ss_100x_json()['data']['multicast_mode'], \
           objects.ss_100x.ss_100x_json()['data']['multicast_timeout']

def arp():
    return objects.ss_100x.ss_100x_json()['data']['arp_timeout'], \
           objects.ss_100x.ss_100x_json()['data']['arp_proxy_enable']

def nat():
    '''Нет Port Forwarding'''
    return objects.ss_100x.ss_100x_json()['data']['nat_enable'], \
           objects.ss_100x.ss_100x_json()['data']['nat_external_ip'], \
           objects.ss_100x.ss_100x_json()['data']['nat_internal_network'], \
           objects.cidr_to_netmask(objects.ss_100x.ss_100x_json()['data']['nat_internal_mask'])

def rip():
    return objects.ss_100x.ss_100x_json()['data']['rip_enable'], \
           objects.ss_100x.ss_100x_json()['data']['rip_gateway_ip'], \
           objects.ss_100x.ss_100x_json()['data']['rip_omit_down_stations'], \
           objects.ss_100x.ss_100x_json()['data']['rip_couple_to_sm_alarms'], \
           objects.ss_100x.ss_100x_json()['data']['rip_routes_cost']

def sntp():
    '''Нет mode'''
    return objects.ss_100x.ss_100x_json()['data']['sntp_ip'], \
           objects.ss_100x.ss_100x_json()['data']['sntp_vlan']

def realtime_bw():
    return objects.ss_100x.ss_100x_json()['data']['realtime_bw_codec'], \
           objects.ss_100x.ss_100x_json()['data']['realtime_bw_threshold'], \
           objects.ss_100x.ss_100x_json()['data']['realtime_bw_timeout']
