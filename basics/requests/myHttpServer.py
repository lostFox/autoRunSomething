#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
import web

urls = (
  '/', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self):
        return "Hello, world!"

if __name__ == "__main__": app.run()
