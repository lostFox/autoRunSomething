#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'

from socket import *
from time import ctime

HOST = ''
PORT = 8001
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
    print('waitting 4 message...')
    data, addr = udpSerSock.recvfrom(BUFSIZ)
    udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
    print('..received from and return to: ', addr)
udpSerSock.close()
