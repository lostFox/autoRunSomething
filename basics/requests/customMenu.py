#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
import requests
import json

import getAT

menu = {
    "button":[
        {
            "name":"公司概况",
            "sub_button":
            [
                {
                    "type":"click",
                    "name":"公司简介",
                    "key":"key00"
                },
                {
                    "type":"click",
                    "name":"业务范围",
                    "key":"key01"
                }
            ]
        },
        {
            "name":"人员查询",
            "sub_button":
            [
                {
                    "type":"click",
                    "name":"珲春公司",
                    "key":"key10"
                },
                {
                    "type":"click",
                    "name":"图们公司",
                    "key":"key11"
                },
                {
                    "type":"click",
                    "name":"龙井公司",
                    "key":"key12"
                },
                {
                    "type":"click",
                    "name":"延吉公司",
                    "key":"key13"
                },

            ]
        },
        {
            "name":"客户服务",
            "sub_button":[
                {
                    "type":"click",
                    "name":"服务接待",
                    "key":"key20"
                },
                {
                    "type":"view",
                    "name":"在线缴费7",
                    "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx794f2868ad431638"
                           "&redirect_uri=http%3A%2F%2F"
                           "vnuxs6.natappfree.cc/jsapi_wx"
                           "&response_type=code&scope=snsapi_base&state=123#wechat_redirect"
                }
            ]
        }
    ]
}

access_token = getAT.getAT();

str = 'https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s' % (access_token)
body = json.dumps(menu, ensure_ascii=False)
response = requests.post(str, data = body)
print response