initial = ['station_route[type]','station_route[title]']

ip_addr = ['station_route[hub_vlan_id]','station_route[addr]','station_route[mask]','station_route[local_access]']

static = ['station_route[hub_vlan_id]','station_route[addr]','station_route[mask]','station_route[gw]']

t_mult = ['station_route[name]','station_route[hub_vlan_id]','station_route[addr]','station_route[mask]',
           'station_route[priority]','station_route[shaper_id]']

r_mult = ['station_route[stream_id]','station_route[hub_vlan_id]']

br_trans = ['station_route[name]','station_route[hub_vlan_id]','station_route[priority]','station_route[shaper_id]']

br_rec = ['station_route[stream_id]','station_route[hub_vlan_id]']

ip_addr_st = ['station_route[vlan]','station_route[addr]','station_route[mask]','station_route[local_access]',
              'station_route[private]','station_route[hub_vlan_id]','station_route[priority]',
              'station_route[shaper_id]']
static_st_lan = ['station_route[vlan]','station_route[addr]','station_route[mask]','station_route[gw]',
             'station_route[private]','station_route[hub_vlan_id]','station_route[priority]','station_route[shaper_id]']

static_st_cntrl = ['station_route[vlan]','station_route[addr]','station_route[mask]','station_route[priority]',
                   'station_route[shaper_id]','station_route[hub_vlan_id]']

static_st_st = ['station_route[vlan]','station_route[priority]','station_route[shaper_id]','station_route[lsid]',
                'station_route[lrid]','station_route[use_custom_addr]','station_route[addr]','station_route[mask]']
