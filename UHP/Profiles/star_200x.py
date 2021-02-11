import requests
from bs4 import BeautifulSoup
from objects import sh_200x
from parser_template import parser_methods
from parser_template import sh_profile


def basic():
    basic = parser_methods(sh_profile['basic'])
    return basic.selects() + basic.checkboxes() + basic.values()

def tdm_rx():
    tdm_rx = parser_methods(sh_profile['tdm_rx'])
    return tdm_rx.select('dj') + tuple(tdm_rx.name_value('db')) + tuple(tdm_rx.name_value('dc'))

def tdm_tx():
    tdm_tx = parser_methods(sh_profile['tdm_tx'])
    return  tuple(tdm_tx.name_value('db')) + tuple(tdm_tx.name_value('dc')) + tdm_tx.select('de') + tdm_tx.check_mode('dg') \
+ tdm_tx.select('df')

def mod():
    mod = parser_methods(sh_profile['mod'])
    return tuple(mod.checkboxes()) + tuple((mod.values()[0] + '.' + mod.values()[1],))

def timing():
    timing = parser_methods(sh_profile['timing'])
    return timing.select('de') + tuple(timing.name_value('df'))

def tlc():
    tlc = parser_methods(sh_profile['tlc'])
    i = list(map(float, tlc.name_value('di')))
    max_tlc = str(i[0]),
    return tlc.check_mode('dh') + max_tlc + tuple(tlc.name_value('db')) + tuple(tlc.name_value('dc')) + \
           tuple((tlc.values()[3] + '.' + tlc.values()[4],)) + tuple((tlc.values()[5] + '.' + tlc.values()[6],))

def tdm_acm():
    tdm_acm = parser_methods(sh_profile['tdm_acm'])
    return tdm_acm.check_mode('db') + tdm_acm.selects() + tuple((tdm_acm.values()[0] + '.' + tdm_acm.values()[1],))

def tdma_rf():
    tdma_rf = parser_methods(sh_profile['tdma_rf'])
    return tuple(tdma_rf.name_value('db')) + tdma_rf.f_sel_text('option') + tdma_rf.check_mode('d6') + tdma_rf.check_mode('d7') \
           + tuple(tdma_rf.name_value('dv')) + tuple(tdma_rf.name_value('dL'))

def tdma_prot():
    tdma_prot = parser_methods(sh_profile['tdma_prot'])
    return tdma_prot.values() + tdma_prot.check_mode('dg')

def tdma_bw():
    tdma_bw = parser_methods(sh_profile['tdma_bw'])
    return tuple(tdma_bw.name_value('db')) + tuple(tdma_bw.name_value('dc')) + tuple(tdma_bw.name_value('dd')) + tuple(tdma_bw.name_value('de')) \
           + tuple(tdma_bw.name_value('df')) + tuple(tdma_bw.name_value('dg')) + tuple(tdma_bw.name_value('dh')) + tuple(tdma_bw.name_value('di')) \
           + tuple(tdma_bw.name_value('dj')) + tuple(tdma_bw.name_value('dk')) + tuple(tdma_bw.name_value('dl')) + tuple(tdma_bw.name_value('dm')) \
           + tuple(tdma_bw.name_value('dn')) + tuple(tdma_bw.name_value('do')) + tuple(tdma_bw.name_value('dp')) + tuple(tdma_bw.name_value('dq')) \
           + tdma_bw.check_mode('dw') + tdma_bw.check_mode('dx') + tdma_bw.check_mode('dy') + tuple(tdma_bw.name_value('dz')) \
           + tdma_bw.check_mode('dv')

def tdma_acm():
    tdma_acm = parser_methods(sh_profile['tdma_acm'])
    return tdma_acm.check_mode('db') + tdma_acm.select('dc') + tdma_acm.check_mode('dh') + tdma_acm.check_mode('di') \
           + tdma_acm.check_mode('dj') + tdma_acm.check_mode('dk') + tdma_acm.check_mode('dl') \
           + tdma_acm.check_mode('dm') + tdma_acm.check_mode('dn') + tdma_acm.check_mode('do') \
           + tdma_acm.check_mode('dp') + tdma_acm.check_mode('dq') + tdma_acm.check_mode('dr') \
           + tdma_acm.check_mode('ds') + tuple((tdma_acm.values()[0] + '.' + tdma_acm.values()[1],))

def roaming():
    roaming = parser_methods(sh_profile['roaming'])
    return roaming.check_mode('db') + tuple(roaming.name_value('dc'))

    # return tdma_acm.check_mode('db') + tdma_acm.select('dc') + tdma_acm.checkings() + tuple((tdma_acm.values()[0] + '.' + tdma_acm.values()[1],))
