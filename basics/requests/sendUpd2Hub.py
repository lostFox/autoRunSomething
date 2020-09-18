#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author:james
@licence: BSD
@file: sendUpd2Hub.py 
@time: 2020/03/08
@contact: lost.Fox2012+py@gmail.com
@site:  
@software: PyCharm 

"""
import socket

# HOSTS = [
#     'apu',
#     'pymotw.com',
#     'www.python.org',
#     'nosuchname',
# ]
#
# for host in HOSTS:
#     print(host)
#     try:
#         name, aliases, addresses = socket.gethostbyname_ex(host)
#         print('  Hostname:', name)
#         print('  Aliases :', aliases)
#         print(' Addresses:', addresses)
#     except socket.error as msg:
#         print('ERROR:', msg)
#     print()

# from urllib.parse import urlparse
#
# URLS = [
#     'http://www.python.org',
#     'https://www.mybank.com',
#     'ftp://prep.ai.mit.edu',
#     'gopher://gopher.micro.umn.edu',
#     'smtp://mail.example.com',
#     'imap://mail.example.com',
#     'imaps://mail.example.com',
#     'pop3://pop.example.com',
#     'pop3s://pop.example.com',
# ]
#
# for url in URLS:
#     parsed_url = urlparse(url)
#     port = socket.getservbyname(parsed_url.scheme)
#     print('{:>6} : {}'.format(parsed_url.scheme, port))

UDP_IP = "255.255.255.255"
UDP_PORT = 29808
MESSAGE = bytes.fromhex('5d750ae75aea3cb9f36b211e9ca77c13422ba2f5d787aeed508f6b21c202909a1b1381c6d8d52b36')

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
# print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                  socket.SOCK_DGRAM) # UDP
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('0.0.0.0', 29809))
sock.settimeout(5)
try:
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    # Receive response
    print('waiting to receive')
    # data, server = sock.recvfrom(4096)
    # print('received {!r}'.format(data))
    data = bytearray(4096)
    nbytes, server = sock.recvfrom_into(data, 4096)
    print('got %d bytes', nbytes)
    print('received {!r}'.format(data))
except socket.timeout:
    print('timeout')
finally:
    sock.close()