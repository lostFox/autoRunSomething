#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
import requests, json

def getAT():
    r = requests.post('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx22571d9ee91f8c0e&secret=ed215bb891e434b103ca53dd45dc9eb0')
    access_token = ''

    if r.ok:
        comments = r.json()
        access_token = comments[u'access_token']

    return access_token