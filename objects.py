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


class star_hub_200x:

    def star_hub_200x_url():
        return 'http://10.0.3.152/'

    def star_hub_200x_json():
        data = {
            "object": "controller",
            "action": "select",
            "id": "52"
        }
        resp = requests.post(options.api_connection_options(), json=data)
        parsed = json.dumps(resp.json(), indent=4, sort_keys=True)
        return json.loads(parsed)


