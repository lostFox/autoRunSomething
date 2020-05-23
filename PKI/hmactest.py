#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import hmac

message = bytes('partner_id=10000&qrcode=cS2nsBRzhW72lQgcGdI6s64YSaaWnxlWtIiU=&sign_method=HMAC&timestamp=20150119130901', 'utf-8')
key = bytes('6c86d9aad103499e9e7148e33af080af', 'utf-8')
h = hmac.new(key, message, digestmod='SHA1')
# 如果消息很长，可以多次调用h.update(msg)
print(h.hexdigest())
