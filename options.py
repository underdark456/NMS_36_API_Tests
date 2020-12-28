import json


def api_connection_options():
    nms = '10.0.3.15'
    token = 'YEdWTCysEactMEzbB7zPAQeeeSVeGqXeFBv0uE3ekq7JW2ck7kkoheFYbzKUYoHc'
    out_type = json
    myurl = f'http://{nms}/jsonapi/?token={token}&out={out_type}'
    return myurl
