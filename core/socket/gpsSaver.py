#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
try:
    #Python 3
    from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
except ImportError:
    import SocketServer      #Python 2
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print( '...connected from:', self.client_address)
        # self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))
        self.wfile.write(b'server out')

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection..')
tcpServ.serve_forever()