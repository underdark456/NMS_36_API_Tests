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

