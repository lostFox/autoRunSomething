#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
import requests, json

def getAT():
    r = requests.post('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx22571d9ee91f8c0e&secret=ed215bb891e434b103ca53dd45dc9eb0')
    # r = requests.post(
    #     'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx794f2868ad431638&secret=047e0c5a5830652051f42c588d3f5648')

    access_token = ''

    if r.ok:
        comments = r.json()
        access_token = comments[u'access_token']

    return access_token

if __name__ == '__main__':
    print('get access token..')
    print(getAT())