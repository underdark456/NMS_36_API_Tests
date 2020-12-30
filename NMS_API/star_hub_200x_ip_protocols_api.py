import objects

def snmp():
    return objects.star_hub_200x.star_hub_200x_json()['data']['snmp_ip1'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['snmp_ip2'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['snmp_read'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['snmp_write']
print(snmp())
def dhcp():
    return objects.star_hub_200x.star_hub_200x_json()['data']['dhcp_enable'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['dhcp_vlan'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['dhcp_ip_start'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['dhcp_ip_end'], \
           objects.cidr_to_netmask(objects.star_hub_200x.star_hub_200x_json()['data']['dhcp_mask']), \
           objects.star_hub_200x.star_hub_200x_json()['data']['dhcp_gw'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['dhcp_dns'], \
           str(objects.star_hub_200x.star_hub_200x_json()['data']['dhcp_lease'])

def dns():
    return objects.star_hub_200x.star_hub_200x_json()['data']['dns_enable'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['dns_clear_timeout']

def arp():
    return objects.star_hub_200x.star_hub_200x_json()['data']['arp_timeout'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['arp_proxy_enable']

def nat():
    '''Нет Port Forwarding'''
    return objects.star_hub_200x.star_hub_200x_json()['data']['nat_enable'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['nat_external_ip'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['nat_internal_network'], \
           objects.cidr_to_netmask(objects.star_hub_200x.star_hub_200x_json()['data']['nat_internal_mask'])

def rip():
    return objects.star_hub_200x.star_hub_200x_json()['data']['rip_enable'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['rip_gateway_ip'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['rip_omit_down_stations'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['rip_couple_to_sm_alarms'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['rip_routes_cost']

def sntp():
    '''Нет mode'''
    return objects.star_hub_200x.star_hub_200x_json()['data']['sntp_ip'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['sntp_vlan']

def tftp():
    return objects.star_hub_200x.star_hub_200x_json()['data']['tftp_ip'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['tftp_vlan']

def multicast():
    return objects.star_hub_200x.star_hub_200x_json()['data']['multicast_mode'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['multicast_timeout']

def acceleration():
    return objects.star_hub_200x.star_hub_200x_json()['data']['accel_enable'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_version'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_svlan_from'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_svlan_to'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_mss'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_max_tcp_window'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_tcp_rcvwnd_update'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_sessions'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_buffers'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_max_queue'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_max_mod_queue'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_retransmit_timeout'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_retransmit_tries'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_inactivity_timeout'], \
           objects.star_hub_200x.star_hub_200x_json()['data']['accel_ack_period']

def ip_screening():
    return objects.star_hub_200x.star_hub_200x_json()['data']['ipscreen_enable']
