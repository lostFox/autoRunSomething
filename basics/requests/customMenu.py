#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
import requests
import json

import getAT

menu = {
	"button":
	[
		{
			"type":"click",
			"name":"公司概况",
			"key":"key0"
		},
		{
			"type":"click",
			"name":"人员查询",
			"key":"key1"
		},
		{
			"type":"click",
			"name":"客户服务",
			"key":"key2"
		}
	]
}

access_token = getAT.getAT();

str = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % (access_token)
body = json.dumps(menu, ensure_ascii=False)
response = requests.post(str, data = body)
print response