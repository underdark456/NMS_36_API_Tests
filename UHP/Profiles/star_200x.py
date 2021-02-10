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
    return tdm_rx.selects() + tdm_rx.checkboxes() + tdm_rx.values() + tdm_rx.checkings()

def tdm_tx():
    tdm_tx = parser_methods(sh_profile['tdm_tx'])
    return  tdm_tx.name_value('db') + tdm_tx.name_value('dc') + tdm_tx.f_sel_text('option') + tdm_tx.check_mode('dg') \
+ tdm_tx.select('df')

def mod():
    mod = parser_methods(sh_profile['mod'])
    return tuple(mod.checkboxes()) + tuple((mod.values()[0] + '.' + mod.values()[1],))

def timing():
    timing = parser_methods(sh_profile['timing'])
    return timing.selects() + timing.values()

def tlc():
    tlc = parser_methods(sh_profile['tlc'])
    return tlc.checkboxes() + tlc.values()

def tdm_acm():
    tdm_acm = parser_methods(sh_profile['tdm_acm'])
    return tdm_acm.checkboxes() + tdm_acm.selects() + tdm_acm.values()

def tdma_rf():
    tdma_rf = parser_methods(sh_profile['tdma_rf'])
    return tdma_rf.name_value('db') + tdma_rf.selects() + tdma_rf.checkboxes() + tdma_rf.values()

