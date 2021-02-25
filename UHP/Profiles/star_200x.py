from objects import sh_profile_url
from parser_template import parser_methods


def basic():
    basic = parser_methods(sh_profile_url('10.0.3.149')['basic'])
    return basic.selects() + basic.checkboxes() + basic.values()

def tdm_rx():
    tdm_rx = parser_methods(sh_profile_url('10.0.3.149')['tdm_rx'])
    return tdm_rx.select('dj') + tdm_rx.name_value('db') + tdm_rx.name_value('dc')

def tdm_tx():
    tdm_tx = parser_methods(sh_profile_url('10.0.3.149')['tdm_tx'])
    return  tdm_tx.name_value('db') + tdm_tx.name_value('dc') + tdm_tx.select('de') + tdm_tx.check_mode('dg') \
+ tdm_tx.select('df')

def mod():
    mod = parser_methods(sh_profile_url('10.0.3.149')['mod'])
    mod_lvl = [i + '.'+ j for i, j in zip(mod.name_value('db'), mod.name_value('dc'))]
    return mod.check_mode('dd') + mod_lvl

def timing():
    timing = parser_methods(sh_profile_url('10.0.3.149')['timing'])
    return timing.select('de') + timing.name_value('df')

def tlc():
    tlc = parser_methods(sh_profile_url('10.0.3.149')['tlc'])
    max_tlc = list(map(float, tlc.name_value('di')))
    max_tlc = ''.join(str(e) for e in max_tlc)
    cn_local = tlc.values()[3] + '.' + tlc.values()[4]
    cn_station = tlc.values()[5] + '.' + tlc.values()[6]
    return tlc.check_mode('dh') + max_tlc.split()  + tlc.name_value('db') + tlc.name_value('dc') + cn_local.split() \
           + cn_station.split()

def tdm_acm():
    tdm_acm = parser_methods(sh_profile_url('10.0.3.149')['tdm_acm'])
    cn_th = tdm_acm.values()[0] + '.' + tdm_acm.values()[1]
    return tdm_acm.check_mode('db') + tdm_acm.selects() +  cn_th.split()


def tdma_rf():
    tdma_rf = parser_methods(sh_profile_url('10.0.3.149')['tdma_rf'])
    modcod = tdma_rf.f_sel_text('option').split()
    return tdma_rf.name_value('db') + modcod + tdma_rf.check_mode('d6') + tdma_rf.check_mode('d7') \
           + tdma_rf.name_value('dv') + tdma_rf.name_value('dL')

def tdma_prot():
    tdma_prot = parser_methods(sh_profile_url('10.0.3.149')['tdma_prot'])
    return tdma_prot.values() + tdma_prot.check_mode('dg')

def tdma_bw():
    tdma_bw = parser_methods(sh_profile_url('10.0.3.149')['tdma_bw'])
    return tdma_bw.name_value('db') + tdma_bw.name_value('dc') + tdma_bw.name_value('dd') + tdma_bw.name_value('de') \
           + tdma_bw.name_value('df') + tdma_bw.name_value('dg') + tdma_bw.name_value('dh') + tdma_bw.name_value('di') \
           + tdma_bw.name_value('dj') + tdma_bw.name_value('dk') + tdma_bw.name_value('dl') + tdma_bw.name_value('dm') \
           + tdma_bw.name_value('dn') + tdma_bw.name_value('do') + tdma_bw.name_value('dp') + tdma_bw.name_value('dq') \
           + tdma_bw.check_mode('dw') + tdma_bw.check_mode('dx') + tdma_bw.check_mode('dy') + tdma_bw.name_value('dz') \
           + tdma_bw.check_mode('dv')

def tdma_acm():
    '''Проверка только по 12 модкодам, добавить легаси'''
    tdma_acm = parser_methods(sh_profile_url('10.0.3.149')['tdma_acm'])
    cn_th = tdma_acm.values()[0] + '.' + tdma_acm.values()[1]
    return tdma_acm.check_mode('db') + tdma_acm.select('dc') + tdma_acm.check_mode('dh') + tdma_acm.check_mode('dl') \
           + tdma_acm.check_mode('dp') + tdma_acm.check_mode('di') + tdma_acm.check_mode('dm') \
           + tdma_acm.check_mode('dq') + tdma_acm.check_mode('dj') + tdma_acm.check_mode('dn') \
           + tdma_acm.check_mode('dr') + tdma_acm.check_mode('dk') + tdma_acm.check_mode('do') \
           + tdma_acm.check_mode('ds') + cn_th.split()

def roaming():
    roaming = parser_methods(sh_profile_url('10.0.3.149')['roaming'])
    return roaming.check_mode('db') + roaming.name_value('dc')

