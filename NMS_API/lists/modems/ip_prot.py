accel = ['accel_enable','accel_version','accel_svlan_from','accel_svlan_to',
         'accel_mss','accel_max_tcp_window','accel_tcp_rcvwnd_update',
         'accel_sessions','accel_buffers','accel_max_queue',
         'accel_max_mod_queue','accel_retransmit_timeout',
         'accel_retransmit_tries','accel_inactivity_timeout',
         'accel_ack_period']

crypto = ['crypto_flags','crypto_key','aes']

dhcp = ['dhcp_enable','dhcp_vlan','dhcp_ip_start',
         'dhcp_ip_end','dhcp_mask','dhcp_gw',
         'dhcp_dns','dhcp_lease']

dns = ['dns_enable','dns_clear_timeout']

screen = ['ipscreen_enable']

snmp = ['snmp_ip1','snmp_ip2','snmp_read','snmp_write']

tftp = ['tftp_ip','tftp_vlan']

multicast = ['multicast_mode','multicast_timeout']

arp = ['arp_timeout','arp_proxy_enable']

nat = ['nat_enable','nat_external_ip','nat_internal_network',
      'nat_internal_mask']

nat_port = ['portmappingexternal_port','portmappinginternal_ip','portmappinginternal_port']

rip = ['rip_enable','rip_routes_cost','rip_update_interval','rip_clear_interval','rip_auth_enable','rip_auth_key',
       'rip_gateway_ip','rip_omit_down_stations','rip_couple_to_sm_alarms']

sntp = ['sntp_mode','sntp_ip','sntp_vlan']

bw = ['realtime_bw_codec','realtime_bw_threshold','realtime_bw_timeout']