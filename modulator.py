import requests
from bs4 import BeautifulSoup
import re


response = requests.get('http://10.0.3.150/cm3?da=1')
soup = BeautifulSoup(response.text, 'lxml')
values = [element['value'] for element in soup.findAll('input', {'type':'text'})]
print(values)



# y = soup.findAll('input', {'type':'text'})
# a = re.findall('(?<=value=")(\d*)',str(y))

# print(a)

# with open("modulator.html", "w",encoding='utf-8') as write_file:
#     write_file.write(str(soup.prettify()))
