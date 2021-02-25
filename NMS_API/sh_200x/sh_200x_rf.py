from objects import sh_200x_json
from NMS_API.lists.modems import rf_setup
from NMS_API.options import values_

def mod():
       return values_(rf_setup.modulator)

def tdm_tx():
       return values_(rf_setup.tdm_tx)


def acm():
       return values_(rf_setup.acm)


def tdm_rx():
       return values_(rf_setup.tdm_rx)

def tdma_rf():
    return sh_200x_json()['data'][rf_setup.tdma_rf[1]], \
           sh_200x_json()['data'][rf_setup.tdma_rf[2]], \
           sh_200x_json()['data'][rf_setup.tdma_rf[3]], \
           sh_200x_json()['data'][rf_setup.tdma_rf[4]], \
           sh_200x_json()['data'][rf_setup.tdma_rf[5]], \
           sh_200x_json()['data'][rf_setup.tdma_rf[6]]

tdma_rf_dict = {'1':'QPSK-2/3','2':'QPSK-5/6','3':'8PSK-2/3','4':'8PSK-5/6','7':'QPSK-1/2','8':'QPSK-3/4'
              ,'11':'8PSK-1/2','12':'8PSK-3/4','13':'16APSK-1/2','14':'16APSK-2/3','15':'16APSK-3/4','16':'16APSK-5/6'}
tdma_modcod = tdma_rf_dict[tdma_rf()[1]] #Нужно для теста.Проблема: Значения в апи и в вебе модема не совпадают.


def tdma_acm():
    return sh_200x_json()['data'][rf_setup.tdma_acm[0]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[1]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[0]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[1]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[2]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[3]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[4]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[5]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[6]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[7]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[8]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[9]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[10]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[2]][rf_setup.tdma_acm_modcod[11]], \
           sh_200x_json()['data'][rf_setup.tdma_acm[3]]

def tdma_prot():
       return values_(rf_setup.tdma_prot)

def tdma_bw():
       return values_(rf_setup.bw_prof)

def roaming():
       return values_(rf_setup.dyn_net)

def tdma_time():
       return values_(rf_setup.tdma_time)

def tlc():
       return values_(rf_setup.tlc)
