#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'

import  web

render = web.template.render('templates/')

urls = (
  '/', 'index'
)

class index:
    def GET(self):
        # return "Hello, world!"
        name = 'Bob'
        return render.index(name)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
