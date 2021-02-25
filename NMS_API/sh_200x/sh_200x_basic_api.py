from objects import sh_200x_json
from NMS_API.lists.modems import basic

def id():
    return sh_200x_json()['data'][basic.id[0]], \
           sh_200x_json()['data'][basic.id[1]]
def mod_que():
    return sh_200x_json()['data'][basic.mod_que[0]], \
           sh_200x_json()['data'][basic.mod_que[1]], \
           sh_200x_json()['data'][basic.mod_que[2]], \
           sh_200x_json()['data'][basic.mod_que[3]], \
           sh_200x_json()['data'][basic.mod_que[4]], \
           sh_200x_json()['data'][basic.mod_que[5]], \
           sh_200x_json()['data'][basic.mod_que[6]], \
           sh_200x_json()['data'][basic.mod_que[7]], \
