# -*- coding: utf-8 -*-

import socket
import ssl
def sina_html():
    sk = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    sk.connect(('www.sina.com.cn',443))
    sk.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n') #报头
    buffer = [] #收取网页数据的列表
    while True:
        ret = sk.recv(10240) #每次收取10240字节
        if ret:
            buffer.append(ret) #每次存放10240字节
        else:    #收完退出
            break
    sk.close()
    new_buffer = b''.join(buffer) #把列表转成字符串
    html = new_buffer.split(b'\r\n\r\n',1) #把报头切出来，得到的是一个列表
    print(html[0].decode('utf-8')) #打印报头
    # with open('web_sina.html','wb') as f:
    #     f.write(html[1]) #把网页存入文件

if __name__ == '__main__':
    sina_html()

