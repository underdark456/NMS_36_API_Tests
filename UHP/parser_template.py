import requests
from bs4 import BeautifulSoup
import objects


class parser_methods():

    def __init__(self,url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'lxml')

    def values(self):
        return tuple([element['value'] for element in self.soup.findAll('input', {'type': 'text'})])

    def checkboxes(self):
        result = list('')
        for element in self.soup.findAll('input', {'type': 'checkbox'}):
            if element.has_attr('name'):
                result.append(element['value'])
        return tuple(result)

    def selects(self):
        return tuple([element['value'] for element in self.soup.findAll('option', selected=True)])

    def checkings(self):
        return tuple([element['value'] for element in self.soup.findAll('input', checked=True)])

    def value(self):
        return tuple(self.soup.find('input')['value'])

    def name_value(self,name):
        return tuple([self.soup.find('input', attrs={'name': f'{name}'})['value']])

    def select(self,name):
        for element in self.soup.find('select', attrs={'name': f'{name}'}):
            if element.has_attr('selected'):
                return tuple([element['value']])




sh_profile = dict({
    'basic' : f'{objects.sh_200x.sh_200x_url()[0]}cb3?da=1',
    'tdm_rx' : f'{objects.sh_200x.sh_200x_url()[0]}cr3?da=1',
    'tdm_tx' : f'{objects.sh_200x.sh_200x_url()[0]}ct3?da=1',
    'mod' : f'{objects.sh_200x.sh_200x_url()[0]}cm3?da=1',
    'timing' : f'{objects.sh_200x.sh_200x_url()[0]}ci3?da=1',
    'tlc' : f'{objects.sh_200x.sh_200x_url()[0]}cl3?da=1',
    'tdm_acm' : f'{objects.sh_200x.sh_200x_url()[0]}ca3?da=1',
    'tdma_rf' : f'{objects.sh_200x.sh_200x_url()[0]}cd3?da=1',
    'tdma_prot' : f'{objects.sh_200x.sh_200x_url()[0]}cp3?da=1',
    'tdma_bw' : f'{objects.sh_200x.sh_200x_url()[0]}cj3?da=1',
    'tdma_acm' : f'{objects.sh_200x.sh_200x_url()[0]}cg3?da=1'
})

#
# test = parser_methods(sh_profile['tdm_tx'])
# print(test.select('de'))





# print(test.values())
# print(test.checkboxes())
# print(test.select())