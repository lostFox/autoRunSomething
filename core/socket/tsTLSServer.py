#! /usr/bin/env python
# -*- coding: UTF-8 -*-

__author__ = 'james'

import BaseHTTPServer, SimpleHTTPServer, os, socket, ssl

script_home = os.path.dirname(os.path.abspath(__file__))
ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close())
      for s in[socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
port = 4443

def main():
    print()

    httpd = BaseHTTPServer.HTTPServer(('127.0.0.1', port), SimpleHTTPServer.SimpleHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile='/james/work/server.crt', server_side=True)
    httpd.serve_forever()

# if __name__ == '__main__':
#     os.chdir(script_home)
main()