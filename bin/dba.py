#!/usr/bin/env python3

""" TODO
- add support for categories .... :^)
- test for correct syntax on CATEGORY
- proper formatted help message
- add info about category when printing search query message
"""

import sys
import requests
import bs4
import json


def search(query, category='soeg/'):
    # 'soeg/' is the default category

    print('|+---> Search: ' + query)

    url = 'https://www.dba.dk/' + category + '?soeg=' + query
    try:
        r = requests.get(url)
    except: # FIXME Specify exception
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

            data_raw = td.script.string
            try:
                data = json.loads(data_raw)
            except json.decoder.JSONDecodeError as e: # FIXME Print nice anyways?
                print('ERROR: json.decoder.JSONDecodeError: %s' % (e))
                print('Raw json:')
                print(data_raw) # Print raw json instead of nicely parsed
                print()
                continue # Skip the rest of this for loop iteration

            print('text:\t' + data['name'])
            print('url:\t' + data['url'])
            print('price:\t' + data['offers']['price'] + ' ' + data['offers']['priceCurrency'])
            print()

    if count == 0:
        print('None\n')


if __name__ == '__main__':
    # Read arguments
    args = sys.argv[1:]

    if not args or args[0] == '--help':
        print('Usage: dba.py [--help] [--category=CATEGORY] [ARGUMENT]...')
        print()
        print('TEST VERSION dba-categories. Adds category support - currently not supporting it though.')
        print('Search www.dba.dk for each argument and print results.')
        print('With --help option: print this and exit.')
        print('By Marcus Larsen')
    else:
        print('dba-categories version. .')
        for arg in args:
            try:
                search(arg)
            except KeyboardInterrupt:
                print()
                break
