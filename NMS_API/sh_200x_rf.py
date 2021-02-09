import objects
from NMS_API.lists.modems import rf_setup

def mod():
    return objects.sh_200x.sh_200x_json()['data'][rf_setup.modulator[0]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.modulator[1]]

def tdm_tx():
    return objects.sh_200x.sh_200x_json()['data'][rf_setup.tdm_tx[0]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdm_tx[1]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdm_tx[2]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdm_tx[3]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdm_tx[4]]

def acm():
    return objects.sh_200x.sh_200x_json()['data'][rf_setup.acm[0]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.acm[1]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.acm[2]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.acm[3]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.acm[4]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.acm[5]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.acm[6]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.acm[7]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.acm[8]]

def tdm_rx():
    return objects.sh_200x.sh_200x_json()['data'][rf_setup.tdm_rx[0]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdm_rx[1]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdm_rx[2]]

def tdma_rf():
    return objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_rf[0]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_rf[1]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_rf[2]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_rf[3]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_rf[4]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_rf[5]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_rf[6]]

def tdma_acm():
    return objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_acm[0]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_acm[1]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_acm[2]]

def tdma_prot():
    return objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_prot[0]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_prot[1]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_prot[2]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_prot[3]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_prot[4]]

def tdma_bw():
    return objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[0]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[1]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[2]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[3]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[4]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[5]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[6]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[7]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[8]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[9]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[10]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[11]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[12]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[13]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[14]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[15]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[16]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[17]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[18]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[19]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.bw_prof[20]]

def dyn_net():
       return objects.sh_200x.sh_200x_json()['data'][rf_setup.dyn_net[0]], \
              objects.sh_200x.sh_200x_json()['data'][rf_setup.dyn_net[1]], \
              objects.sh_200x.sh_200x_json()['data'][rf_setup.dyn_net[2]]

def tdma_time():
       return objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_time[0]], \
              objects.sh_200x.sh_200x_json()['data'][rf_setup.tdma_time[1]],

def tlc():
    return objects.sh_200x.sh_200x_json()['data'][rf_setup.tlc[0]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tlc[1]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tlc[2]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tlc[3]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tlc[4]], \
           objects.sh_200x.sh_200x_json()['data'][rf_setup.tlc[5]]

