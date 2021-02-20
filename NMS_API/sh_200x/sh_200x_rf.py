from objects import sh_200x_json
from NMS_API.lists.modems import rf_setup

def mod():
    return sh_200x_json()['data'][rf_setup.modulator[0]], \
           sh_200x_json()['data'][rf_setup.modulator[1]]

def tdm_tx():
    return sh_200x_json()['data'][rf_setup.tdm_tx[0]], \
           sh_200x_json()['data'][rf_setup.tdm_tx[1]], \
           sh_200x_json()['data'][rf_setup.tdm_tx[2]], \
           sh_200x_json()['data'][rf_setup.tdm_tx[3]], \
           sh_200x_json()['data'][rf_setup.tdm_tx[4]]

def acm():
    return sh_200x_json()['data'][rf_setup.acm[0]], \
           sh_200x_json()['data'][rf_setup.acm[1]], \
           sh_200x_json()['data'][rf_setup.acm[2]], \
           sh_200x_json()['data'][rf_setup.acm[3]], \
           sh_200x_json()['data'][rf_setup.acm[4]], \
           sh_200x_json()['data'][rf_setup.acm[5]], \
           sh_200x_json()['data'][rf_setup.acm[6]], \
           sh_200x_json()['data'][rf_setup.acm[7]], \
           sh_200x_json()['data'][rf_setup.acm[8]]

def tdm_rx():
    return sh_200x_json()['data'][rf_setup.tdm_rx[0]], \
           sh_200x_json()['data'][rf_setup.tdm_rx[1]], \
           sh_200x_json()['data'][rf_setup.tdm_rx[2]]

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
    return sh_200x_json()['data'][rf_setup.tdma_prot[0]], \
           sh_200x_json()['data'][rf_setup.tdma_prot[1]], \
           sh_200x_json()['data'][rf_setup.tdma_prot[2]], \
           sh_200x_json()['data'][rf_setup.tdma_prot[3]], \
           sh_200x_json()['data'][rf_setup.tdma_prot[4]]

def tdma_bw():
    return sh_200x_json()['data'][rf_setup.bw_prof[0]], \
           sh_200x_json()['data'][rf_setup.bw_prof[1]], \
           sh_200x_json()['data'][rf_setup.bw_prof[2]], \
           sh_200x_json()['data'][rf_setup.bw_prof[3]], \
           sh_200x_json()['data'][rf_setup.bw_prof[4]], \
           sh_200x_json()['data'][rf_setup.bw_prof[5]], \
           sh_200x_json()['data'][rf_setup.bw_prof[6]], \
           sh_200x_json()['data'][rf_setup.bw_prof[7]], \
           sh_200x_json()['data'][rf_setup.bw_prof[8]], \
           sh_200x_json()['data'][rf_setup.bw_prof[9]], \
           sh_200x_json()['data'][rf_setup.bw_prof[10]], \
           sh_200x_json()['data'][rf_setup.bw_prof[11]], \
           sh_200x_json()['data'][rf_setup.bw_prof[12]], \
           sh_200x_json()['data'][rf_setup.bw_prof[13]], \
           sh_200x_json()['data'][rf_setup.bw_prof[14]], \
           sh_200x_json()['data'][rf_setup.bw_prof[15]], \
           sh_200x_json()['data'][rf_setup.bw_prof[16]], \
           sh_200x_json()['data'][rf_setup.bw_prof[17]], \
           sh_200x_json()['data'][rf_setup.bw_prof[18]], \
           sh_200x_json()['data'][rf_setup.bw_prof[19]], \
           sh_200x_json()['data'][rf_setup.bw_prof[20]]

def roaming():
       return sh_200x_json()['data'][rf_setup.dyn_net[0]], \
              sh_200x_json()['data'][rf_setup.dyn_net[1]]

def tdma_time():
       return sh_200x_json()['data'][rf_setup.tdma_time[0]], \
              sh_200x_json()['data'][rf_setup.tdma_time[1]],

def tlc():
    return sh_200x_json()['data'][rf_setup.tlc[0]], \
           sh_200x_json()['data'][rf_setup.tlc[1]], \
           sh_200x_json()['data'][rf_setup.tlc[2]], \
           sh_200x_json()['data'][rf_setup.tlc[3]], \
           sh_200x_json()['data'][rf_setup.tlc[4]], \
           sh_200x_json()['data'][rf_setup.tlc[5]]

