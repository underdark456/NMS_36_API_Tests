import objects


def snmp():
    return objects.star_hub_200x_json()['data']['snmp_ip1'], \
           objects.star_hub_200x_json()['data']['snmp_ip2'], \
           objects.star_hub_200x_json()['data']['snmp_read'], \
           objects.star_hub_200x_json()['data']['snmp_write']


def dhcp():
    '''join converts /xx mask to cidr(like 255.255.255.9)'''
    return objects.star_hub_200x_json()['data']['dhcp_enable'], \
           objects.star_hub_200x_json()['data']['dhcp_vlan'], \
           objects.star_hub_200x_json()['data']['dhcp_ip_start'], \
           objects.star_hub_200x_json()['data']['dhcp_ip_end'], \
           '.'.join(
               [str((0xffffffff << (32 - int((objects.star_hub_200x_json()['data']['dhcp_mask']))) >> i) & 0xff) for i
                in [24, 16, 8, 0]]), \
           objects.star_hub_200x_json()['data']['dhcp_gw'], \
           objects.star_hub_200x_json()['data']['dhcp_dns'], \
           str(objects.star_hub_200x_json()['data']['dhcp_lease'])


def dns():
    return objects.star_hub_200x_json()['data']['dns_enable'], \
           objects.star_hub_200x_json()['data']['dns_clear_timeout']
