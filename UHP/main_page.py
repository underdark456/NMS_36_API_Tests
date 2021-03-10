import re
from parser_template import parser_methods

def sw_version(ip):
    p = parser_methods(f'http://{ip}/cc40')
    search = p.soup.find('b',text = re.compile('(\d\.\d\.\d)'))
    return search.text


