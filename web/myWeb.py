#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'

import  web

render = web.template.render('templates/')

urls = (
    '/(.*)/', 'redirect',
    '/(.*)', 'index'
)

db = web.database(dbn='sqlite', db='mydata')

class index:
    def GET(self, name):
        i = web.input(name=None)
        return render.index(i.name)

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
