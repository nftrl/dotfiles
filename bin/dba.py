#!/usr/bin/env python3

import argparse
import requests
from bs4 import BeautifulSoup
import json

baseurl = "https://www.dba.dk/soeg/?soeg="

# (argparse) read search query from command line arguments
# (requests) get .html from dba.dk
# (bs4) search .html for class listingLink
# print results (article, price, date, link)

args = ['bastl', 'monotron', 'volca']

for arg in args:
    print('Search: ' + arg)
    url = baseurl + arg
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    count = 0
    for td in soup.find_all('td'):
        if td.get('class') and 'mainContent' in td.get('class'):
            count += 1
            data = json.loads(td.script.string)

            print(data['name'])
            print('url:\t' + data['url'])
            print('price:\t' + data['offers']['price'] + data['offers']['priceCurrency'])
            print('')   # newline

    if count == 0:
        print('None\n')
