from objects import sh_200x_json


def values_(params):
    values = list()
    for param in params:
        values.append(sh_200x_json()['data'][param])
    return values