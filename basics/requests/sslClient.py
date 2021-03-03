# -*- coding: utf-8 -*-

import socket, ssl, pprint, time

HOST = 'www.mynginx.com'
# HOST = '127.0.0.1'
PORT = 443
BUFSIZE = 1024
ADDR = (HOST, PORT)

# socket create success
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# require a certificate from the server

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


ssl_sock = ssl.wrap_socket(s, ca_certs='./rootCA.pem', cert_reqs=ssl.CERT_REQUIRED)
# socket connect success
try:
    ssl_sock.connect(ADDR)

# note that closing the SSLSocket will also close the underlying socket
    pprint.pprint(ssl_sock.getpeercert())
    ssl_sock.send(b'GET / HTTP/1.1\r\n111\r\nConnection: close\r\n\r\n')
    msg = ssl_sock.recv(1024).decode("utf-8")
    print("receive msg from server : {%1}", msg)
# while True:
#     data = raw_input('> ')
#     if not data:
#         break
#     ssl_sock.send(data)
#     data = ssl_sock.recv(BUFSIZE)
#     if not data:
#         break
#     print data
finally:
    ssl_sock.close()
