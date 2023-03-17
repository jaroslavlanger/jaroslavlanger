#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Examples of python regex for url

2021 Feb 08, Jaroslav Langer
"""

import requests
import re


# https://regexr.com/39nr7
# /[(http(s)?):\/\/(www\.)?a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/ig

# https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url
# regex_url = r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

# Simple
# pattern = r'[a-z]{1,256}\.[a-z]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

# More advanced
# pattern = r'[-a-zA-Z0-9@:%._\+~#=]{1,265}\.[a-zA-Z0-9()]{1,6}'

# From stackoverflow
pattern = r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)'

# Try with domain alternation
pattern = r'([-a-zA-Z0-9@:%._\+~#=]{1,256}\.(cz|com)\b)'

# Domains from list
domains_list = ['CZ', 'com']
# print('domains', '|'.join(domains_list))

# Works good, but .css and .svg in the resutls
pattern_url = r'[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*'

# REAL STUFF

# Download domains form iana.org
resp_tlds = requests.request(method='get', url='https://data.iana.org/TLD/tlds-alpha-by-domain.txt')

# Remove first line (date), last line (empty)
tlds = resp_tlds.text.split('\n')[1:-1]

# hostname = r'[(http(s)?):\/\/(www\.)?-a-zA-Z0-9@:%._\+~#=]{1,256}'
scheme = r'(https?)?:?\/*(www\.)?'
user = r'[-a-zA-Z0-9._+~=]{1,256}@'
host = r'[-a-zA-Z0-9._+~=]{1,256}'
port = r':[0-9]{0,5}'
domains = '|'.join(tlds)                        # domains = '|'.join(domains_list)
path = r'([-a-zA-Z0-9()@:%_\+.~&//=]*)'
query_fragment = r'((\?|\#)[-a-zA-Z0-9()@:%_\+.~#?&//=]*)?'


pattern_url = fr'{scheme}(({user})?{host}({port})?\.({domains})\b{path}){query_fragment}'
# print('pattern', pattern_url)

# from fit_cvut_cz_short import fit_html_str
# from fit_cvut_cz import fit_html_str
from fit_cvut_cz_full import fit_html_str

prog = re.compile(pattern_url, flags=re.IGNORECASE)
findings = prog.findall(fit_html_str)
print('findings:', findings)

links = {tup[2] for tup in findings}
print(links)

if any(['mit.edu' in link for link in links]):
    print('\n    HEUREKA!\n')

visited = set()

for url in links:
    # url = link.split('//', maxsplit=1)[-1]
    url = f'http://{url}'
    print(url)
    # resp = requests.request(mathod='get', url)


