import json
import requests

def star_hub_json():
    nms = '10.0.3.15'
    token = '46aa0a8c'
    out_type = json
    myurl = f'http://{nms}/jsonapi/?token={token}&out={out_type}'
    data = {
        "object": "controller",
        "action": "select",
        "id": "2"
    }
    return requests.post(myurl, json=data)
def star_hub_txlvl():
    resp = star_hub_json()
    parsed = json.dumps(resp.json(), indent=4, sort_keys=True)
    json_string_data = json.loads(parsed)
    return float(json_string_data['data']['modulator_txlvl'])




# with open("data_file.json", "w") as write_file:
#       write_file.write(parsed)
