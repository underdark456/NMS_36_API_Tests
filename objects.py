import requests
import json
import options


def star_hub_200x_json():
    data = {
        "object": "controller",
        "action": "select",
        "id": "2"
    }
    resp = requests.post(options.api_connection_options(), json=data)
    parsed = json.dumps(resp.json(), indent=4, sort_keys=True)
    return json.loads(parsed)


