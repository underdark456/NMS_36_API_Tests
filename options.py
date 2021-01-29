import json


def nms_connection_options():
    nms = '10.0.3.16'
    nms_login = 'http://10.0.3.16/login/'
    token = '3db734be'
    out_type = json
    myurl = f'http://{nms}/jsonapi/?token={token}&out={out_type}'
    return myurl, nms_login

