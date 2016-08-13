#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
try:
    from SocketServer import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
except ImportError:
    from socketserver import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 8000
ADDR = (HOST, PORT)

class myRequestHandle(SRH):
    def handle(self):
        print('...connected from: ', self.client_address)
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, myRequestHandle)
print("waitting 4 connection...")
tcpServ.serve_forever()
