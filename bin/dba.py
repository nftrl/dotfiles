#!/usr/bin/env python3

import sys
import requests
import bs4
import json

baseurl = "https://www.dba.dk/soeg/?soeg="

# Read arguments
args = sys.argv[1:]

if not args or args[0] == '--help':
    print('Usage: dba.py [--help] [ARGUMENT]...')
    print()
    print('Search www.dba.dk for each argument and print results.')
    print('With --help option: print this and exit.')
    print('By Marcus Larsen')
else:
    for arg in args:
        print('|+---> Search: ' + arg)

        url = baseurl + arg
        try:
            r = requests.get(url)
        except KeyboardInterrupt:
            print()
            break
        except:
            print()
            print('An error occurred during requests.get(%s)' % (url))
            print('Do you have an internet connection?')
            print()
            raise

        try:
            soup = bs4.BeautifulSoup(r.text, "lxml")
        except bs4.FeatureNotFound: # If lxml is not found, try with html.parser
            try:
                soup = bs4.BeautifulSoup(r.text, "html.parser")
            except bs4.FeatureNotFound: # If html.parser is not found, try with whatever
                soup = bs4.BeautifulSoup(r.text)

        count = 0
        for td in soup.find_all('td'):
            if td.get('class') and 'mainContent' in td.get('class'):
                count += 1
                data = json.loads(td.script.string)

                print('text:\t' + data['name'])
                print('url:\t' + data['url'])
                print('price:\t' + data['offers']['price'] + data['offers']['priceCurrency'])
                print()   # newline

        if count == 0:
            print('None\n')
