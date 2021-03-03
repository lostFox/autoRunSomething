#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
import base64

encoded = base64.b64encode('data to be encoded')
print(encoded)

data = base64.b64decode(encoded)
print(data)

print(base64.encodestring(data))