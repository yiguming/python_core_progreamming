#!/usr/bin/env python
#-*-coding:utf-8-*-

import socket,sys

website = sys.argv[1]
port = 80
print website

print "Creating socket...",
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "done."

print "Connecting to ...",
s.connect((website,port))
print "done."

s.send("GET /index.html HTTP/1.0\r\n\r\n")
data = s.recv(4096)
print data
