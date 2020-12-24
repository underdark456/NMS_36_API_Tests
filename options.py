import json


def api_connection_options():
    nms = '10.0.3.15'
    token = '46aa0a8c'
    out_type = json
    myurl = f'http://{nms}/jsonapi/?token={token}&out={out_type}'
    return myurl
