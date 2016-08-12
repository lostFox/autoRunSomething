#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# import socket
from socket import *

__author__ = 'james'
from time import ctime

#tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#udpSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
tcpSerSock = socket(AF_INET, SOCK_STREAM)
udpSock = socket(AF_INET, SOCK_DGRAM)

HOST = ''
PORT = 8000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print 'waiting 4 connection...'
    tcpCommSock, addr = tcpSerSock.accept()
    print '...connected from: ', addr

    while True:
        data = tcpCommSock.recv(BUFSIZ)
        if not data:
            break;
        tcpCommSock.send('[%s] %s' % (ctime(), data))

    tcpCommSock.close()
tcpSerSock.close()