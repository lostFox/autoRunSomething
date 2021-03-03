#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
import requests
import json

import getAT

access_token = getAT.getAT();

str = 'https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s' % (access_token)

response = requests.post(str)
print response