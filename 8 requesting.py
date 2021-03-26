from requests import get
import bs4
import lxml
import re
from PIL import Image
'''
website = get('https://en.wikipedia.org/wiki/Estonia')

unpacked = bs4.BeautifulSoup(website.text,'lxml')
tableofcontents = []
for toc in unpacked.select('.toctext'):
    tableofcontents.append(toc.text)
print(tableofcontents)
'''

images = []
no404 = True
while no404:
    for year in range(2014,2021):
        n = year
        for month in range(1,12):
            n2 = month
            leht = f'https://www.real.edu.ee/ajaveeb/140a/{n}/{n2}/'
            site = get(leht)
            htm = bs4.BeautifulSoup(site.text,'lxml')
            print(site)
            if 'Viga 404 - Otsitut ei leitud!' in site.text:
                pass
            else:
                for img in htm.select('img'):
                    images.append(img)
    no404 = False
for picture in images:
    print(picture['src'])



