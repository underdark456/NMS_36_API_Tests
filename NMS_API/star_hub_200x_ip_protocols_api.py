import objects

def acceleration():
    return objects.sh_200x.sh_200x_json()['data']['accel_enable'], \
           objects.sh_200x.sh_200x_json()['data']['accel_version'], \
           objects.sh_200x.sh_200x_json()['data']['accel_svlan_from'], \
           objects.sh_200x.sh_200x_json()['data']['accel_svlan_to'], \
           objects.sh_200x.sh_200x_json()['data']['accel_mss'], \
           objects.sh_200x.sh_200x_json()['data']['accel_max_tcp_window'], \
           objects.sh_200x.sh_200x_json()['data']['accel_tcp_rcvwnd_update'], \
           objects.sh_200x.sh_200x_json()['data']['accel_sessions'], \
           objects.sh_200x.sh_200x_json()['data']['accel_buffers'], \
           objects.sh_200x.sh_200x_json()['data']['accel_max_queue'], \
           objects.sh_200x.sh_200x_json()['data']['accel_max_mod_queue'], \
           objects.sh_200x.sh_200x_json()['data']['accel_retransmit_timeout'], \
           objects.sh_200x.sh_200x_json()['data']['accel_retransmit_tries'], \
           objects.sh_200x.sh_200x_json()['data']['accel_inactivity_timeout'], \
           objects.sh_200x.sh_200x_json()['data']['accel_ack_period']

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

