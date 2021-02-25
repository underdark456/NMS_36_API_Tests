from parser_template import parser_methods as p
from objects import sh_200x_url

def SNMP(url):
    snmp = p(url)
    return snmp.values()

def DHCP(url):
    dhcp = p(url)
    return dhcp.select('de') + dhcp.values()


def DNS(url):
    dns = p(url)
    return dns.check_mode('da') + dns.values()


def ARP(url):
    arp = p(url)
    return arp.values() + arp.check_mode('db')


def NAT(url):
    """не реализован порт форвард в апи нмса"""
    nat = p(url)
    return nat.check_mode('di') + nat.name_value('if') + nat.name_value('ih') + nat.name_value('mg')


def RIP(url):
    rip = p(url)
    return rip.check_mode('db') + rip.name_value('ia') + rip.check_mode('dc') + rip.check_mode('dd') + rip.name_value(
        'de')


def SNTP(url):
    """В апи нмс не реализован mode"""
    sntp = p(url)
    return sntp.select('db') + sntp.values()


def TFTP(url):
    tftp = p(url)
    return tftp.values()


def Multicast(url):
    multicast = p(url)
    return multicast.select('db') + multicast.values()


def Acceleration(url):
    acceleration = p(url)
    return acceleration.check_mode('da') + acceleration.select('dq') + acceleration.values()


def Screening(url):
    screening = p(url)
    return screening.select('dc')
