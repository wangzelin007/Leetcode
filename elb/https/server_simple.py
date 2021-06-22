# coding: utf-8
# !/usr/bin/python
import BaseHTTPServer, SimpleHTTPServer
import ssl
httpd = BaseHTTPServer.HTTPServer(('127.0.0.1, 20000'), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile='./server_key.pem', server_side=True)
httpd.serve_forever()