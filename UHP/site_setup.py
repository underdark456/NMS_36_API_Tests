from parser_template import parser_methods
from objects import sh_profile_url

def site_name(ip):
    site_name = parser_methods(sh_profile_url(ip)['site_setup'])
    return site_name.name_value('td')

def location(ip):
    '''Lat + deg + min + Long + deg + min'''
    location = parser_methods(sh_profile_url(ip)['site_setup'])
    return location.name_value('du') + location.name_value('dv') + list(location.select('dw')) \
            + location.name_value('dx') + location.name_value('dy') + list(location.select('dz'))

def mid(ip):
    '''Rx1 + Rx2 + Transmit + Power + Transmit + 10MhzRx + 10MhzTx + SpInvRx1 + SpInvRx2 + SpInvTx +
    FreqAdjRx1 + FreqAdjRx2 + FreqAdjTx'''
    mid = parser_methods(sh_profile_url(ip)['site_setup'])
    return mid.name_value('df') + mid.name_value('de') + mid.name_value('dd') \
+ mid.check_mode('dn') + mid.check_mode('dg') + mid.check_mode('do') \
+ mid.check_mode('dh') + mid.check_mode('dp') + mid.check_mode('dm') \
+ mid.check_mode('di') + mid.name_value('dr') + mid.name_value('dq') \
+ mid.name_value('dk')

def bottom(ip):
    ''' SCPC_mode + TDMA mode + NET_ID + RF_ID + Gloabal_TX'''
    '''TDMA_mode: 0 - 6, 1 - 12, 2 -24, 3 - 40'''
    bottom = parser_methods(sh_profile_url(ip)['site_setup'])
    return bottom.name_value('dt') + bottom.select('ds') + bottom.name_value('dc') + bottom.name_value('db') \
+ bottom.name_value('dl')

