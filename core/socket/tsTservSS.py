#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
try:
    #Python 3
    from socketserver import (ThreadingTCPServer as TCP,
                          StreamRequestHandler as SRH)
except ImportError:
    import SocketServer      #Python 2
# from time import ctime
import time
import _thread
import urllib.parse
import re, json

HOST = '0.0.0.0'

appPORT = 9007
redFlagPORT = 9303
bentengPORT = 9409

BUFSIZE = 1024

tboxCount = 0
# tboxDic   = {tboxCount:None, }
tboxDic = []
appCount  = 0
appMsgDic = {appCount:"", }

# flag = 0

index_content = '''
HTTP/1.x 200 ok
Content-Type: text/html

'''

notfind_content = '''
HTTP/1.x 404 
Content-Type: text/html

no car find
'''

class MyEchoHandler(SRH):
    def handle(self):
        global tboxCount, tboxDic, appMsgDic
        print( '...connected from:', self.client_address)
        # self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))
        tboxCount += 1
        # tboxDic[tboxCount] = self.request
        tid = tboxCount
        tboxDic.append(tid)
        # self.wfile.write(bytes(self.client_address[0],'utf-8'))
        flag = True
        while True:
            # self.data = self.rfile.readline().strip()
            msg = self.request.recv(BUFSIZE)
            if flag:
                msg = bytes("your id:" + str(tid), 'utf-8')
                flag = False
            elif tid not in appMsgDic.keys():
                msg = msg
            else:
                msg = bytes(appMsgDic[tid], 'utf-8')
                del appMsgDic[tid]
            if not msg:
                break
            self.request.send(msg)
        tboxCount -= 1
        self.wfile.write(b'server out')

def startEchoServer(server):
    print('waiting for connection..')
    server.serve_forever()

class MyCmdHandler(SRH):
    def handle(self):
        global tboxDic, appMsgDic
        #appCount += 1

        msg = self.request.recv(BUFSIZE)
        intCount = 0
        try:
            # # print(msg)
            # msg_str = msg.decode()
            # # print('recv special: ', msg_str)
            # kv = msg_str.split('\r\n\r\n')[1]
            # tid = kv.split('=')[1]
            #
            # intCount = int(tid)
            strRecv = bytes.decode(msg)
            print('recv special: ', strRecv)
            intCount = int(strRecv)

        finally:
            if intCount != 0 and intCount in tboxDic:#.keys():
                appMsgDic[intCount] = "^^^^^^^^^^^^^^^one cmd be called 2 this client $$$$$$$$$$$$$$$$$$$"
                self.request.send(index_content.encode())
            else:
                self.request.send(notfind_content.encode())
            #appCount -= 1


def startAppServer(server):
    server.serve_forever()

if __name__ == '__main__':
    TCP.allow_reuse_address = True
    tcpServ = TCP((HOST, redFlagPORT), MyEchoHandler)
    _thread.start_new_thread(startEchoServer, (tcpServ, ))

    httpServ = TCP((HOST, appPORT), MyCmdHandler)
    _thread.start_new_thread(startAppServer, (httpServ, ))

    while True:
        pass
        # time.sleep(5)
        #
        # if tboxDic[0] != None:
        #     flag = 1

#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'
from SocketServer import (TCPServer as TCP,
                          StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 21567
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
    def handle(self):
        print( '...connected from:', self.client_address)
        self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))

tcpServ = TCP(ADDR, MyRequestHandler)
print('waiting for connection..')
tcpServ.serve_forever()