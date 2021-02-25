import requests
from bs4 import BeautifulSoup


class parser_methods():

    def __init__(self,url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'lxml')

    def values(self):
        return list([element['value'] for element in self.soup.findAll('input', {'type': 'text'})])

    def checkboxes(self):
        result = list('')
        for element in self.soup.findAll('input', {'type': 'checkbox'}):
            if element.has_attr('name'):
                result.append(element['value'])
        return result

    def selects(self):
        return [element['value'] for element in self.soup.findAll('option', selected=True)]

    def checkings(self):
        return [element['value'] for element in self.soup.findAll('input', checked=True)]

    def value(self):
        for i in self.soup.findAll('input', type=lambda x: x != 'hidden'):
            return i['value']

    def name_value(self,name):
            return [self.soup.find('input', attrs={'name': f'{name}'})['value']]

    def select(self,name):
        for element in self.soup.find('select', attrs={'name': f'{name}'}):
            if element.has_attr('selected'):
                return list(element['value'])

    def f_sel_text(self,name):
        return self.soup.find(f'{name}', selected=True).text

    def check_mode(self,name):
        if 'checked' in self.soup.find('input',{"name":f"{name}"}).attrs:
            return list('1')
        else:
            return list('0')


