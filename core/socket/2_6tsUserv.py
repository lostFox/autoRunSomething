#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
from socket import *
from time import ctime

HOST = ''
PORT = 16688
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print 'waiting for message...'
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    # udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    # print '... received from add returned to:', addr
    print 'recv: ', data
udpSerSock.close()