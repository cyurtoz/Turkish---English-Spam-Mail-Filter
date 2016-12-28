#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 22:17:46 2016

@author: cyurtoz
"""

import requests
def post(sentence):
    headers = {'Content-type': 'application/json'}
    r = requests.post('http://localhost:9090/lemmatize',verify=False, headers=headers, json={"text": sentence})
    if 'result' in r.json():
        return r.json()['result']
    else:
        return ''
