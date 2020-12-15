import json
import requests

nms = '10.0.3.15'
token = '46aa0a8c'
out_type = json
myurl = f'http://{nms}/jsonapi/?token={token}&out={out_type}'

data = {
    "object": "controller",
    "action": "select",
    "id": "2"
}

resp = requests.post(myurl, json=data)
parsed = json.dumps(resp.json(), indent=4, sort_keys=True)

# with open("data_file.json", "w") as write_file:
#      write_file.write(parsed)
