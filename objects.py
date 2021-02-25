import requests
import json
import options


def cidr_to_netmask(cidr):
  cidr = int(cidr)
  mask = (0xffffffff >> (32 - cidr)) << (32 - cidr)
  return (str( (0xff000000 & mask) >> 24)   + '.' +
          str( (0x00ff0000 & mask) >> 16)   + '.' +
          str( (0x0000ff00 & mask) >> 8)    + '.' +
          str( (0x000000ff & mask)))


def sh_200x_url():
    url_uhp = 'http://10.0.3.149/'
    url_ip_protocols = 'http://10.0.3.16/#/controller_configure/2/#tab4'
    return url_uhp, url_ip_protocols


def sh_200x_json():
    data = {
        "object": "controller",
        "action": "select",
        "id": "2"
    }
    resp = requests.post(options.nms_connection_options()[0], json=data)
    parsed = json.dumps(resp.json(), indent=4, sort_keys=True)
    return json.loads(parsed)

def sh_profile_url(ip):
    return dict({
    'basic' : f'http://{ip}/cb3?da=1',
    'tdm_rx' : f'http://{ip}/cr3?da=1',
    'tdm_tx' : f'http://{ip}/ct3?da=1',
    'mod' : f'http://{ip}/cm3?da=1',
    'timing' : f'http://{ip}/ci3?da=1',
    'tlc' : f'http://{ip}/cl3?da=1',
    'tdm_acm' : f'http://{ip}/ca3?da=1',
    'tdma_rf' : f'http://{ip}/cd3?da=1',
    'tdma_prot' : f'http://{ip}/cp3?da=1',
    'tdma_bw' : f'http://{ip}/cj3?da=1',
    'tdma_acm' : f'http://{ip}/cg3?da=1',
    'roaming' : f'http://{ip}/co3?da=1',
    'site_setup': f'http://{ip}/cc2'
})

def ip_prot_url(ip):
    return dict({
        'snmp': f'http://{ip}/cc9',
        'dhcp': f'http://{ip}/cc8',
        'dns': f'http://{ip}/cc59',
        'arp': f'http://{ip}/cc23',
        'nat': f'http://{ip}/cc7',
        'rip': f'http://{ip}/cc10',
        'sntp': f'http://{ip}/cc11',
        'rtp': f'http://{ip}/ss38',
        'tftp': f'http://{ip}/cc21',
        'gtp': f'http://{ip}/ss62',
        'multicast': f'http://{ip}/cc39',
        'acceleration': f'http://{ip}/cc12',
        'other': f'http://{ip}/cc13'
    })

def ss_100x_url():
    url_uhp = 'http://10.0.3.155/'
    url_ip_protocols ='http://10.0.3.16/#/remote/4/update/?net_id=1#tab2'
    return url_uhp, url_ip_protocols


def ss_100x_json():
    data = {
        "object": "station",
        "action": "select",
        "id": "4"
    }
    resp = requests.post(options.nms_connection_options()[0], json=data)
    parsed = json.dumps(resp.json(), indent=4, sort_keys=True)
    return json.loads(parsed)

