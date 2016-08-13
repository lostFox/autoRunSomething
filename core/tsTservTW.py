#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connect from: ', clnt)

    def dataReceived(self, data):
        self.transport.write('[%s] %s' %(ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServProtocol
print('waittting for connection...')
reactor.listenTCP(PORT, factory)
reactor.run()
