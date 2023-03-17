#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Examples of python regex for url

2021 Feb 08, Jaroslav Langer
"""

import requests
import re

from url_facebook.facebook_html import facebook_html_str
from url_fit_cvut.fit_cvut_cz_full import fit_html_str

def get_tlds():
    # Download domains form iana.org
    resp_tlds = requests.request(method='get', url='https://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    # Remove first line (date), last line (empty)
    tlds = resp_tlds.text.split('\n')[1:-1]
    return tlds


def get_url_regex_obj():
    tlds = get_tlds()


    scheme = r'(https?)?:?\/*(www\.)?'

    sou = r'(\s|\A|\(|\{|\[|\'|\")' # START OF URL''
    user = r'[-a-zA-Z0-9._+~]{1,256}@'
    host = r'[-a-zA-Z0-9._+~]{1,256}'
    port = r':[0-9]{0,5}'
    domains = '|'.join(tlds)
    path = r'/[-a-zA-Z0-9()@:%_+.~&=/]*'
    query_fragment = r'((\?|\#)[-a-zA-Z0-9()@:%_\+.~#?&//=]*)?'
    eou = r'(\s|\Z|\)|\}|\]|\'|\")' # END OF URL

    pattern_url = fr'{sou}{scheme}(({user})?{host}({port})?\.({domains})({path})?){query_fragment}{eou}'

    return re.compile(pattern_url, flags=re.IGNORECASE)

if __name__ == "__main__":

    url_regex_obj = get_url_regex_obj()

    # text = fit_html_str
    text = facebook_html_str
    # print(text)

    findings = url_regex_obj.findall(text)
    # print(findings)

    links = {f'https://{tup[3][:-1]}' if (tup[3].endswith('/')) else f'https://{tup[3]}' for tup in findings}
    links = {f'https://{tup[3]}' for tup in findings}
    print()
    print(sorted(links))
