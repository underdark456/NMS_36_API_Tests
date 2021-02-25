from parser_template import parser_methods
from objects import sh_profile_url

def site_name():
    site_name = parser_methods(sh_profile_url('10.0.3.149')['site_setup'])
    return site_name.name_value('td')

def location():
    location = parser_methods(sh_profile_url('10.0.3.149')['site_setup'])
    return location.name_value('du') + location.name_value('dv') + list(location.select('dw'))

