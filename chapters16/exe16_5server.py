#!/usr/bin/env python
from socket import *
from time import ctime
import os

HOST = ''
PORT = 50008

server = socket(AF_INET,SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)

conn,addr = server.accept()
print 'Contented by' ,addr
while True:
    data = conn.recv(1024)
    if data == "data":
        data  = '%s' % ctime()
    elif data == "os":
        data  = os.name
    elif data == "ls":
        data = "%s" % os.listdir(os.curdir)
    else:
        break
    conn.sendall(data)
conn.close()




