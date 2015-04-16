#!/usr/bin/env python
from socket import *

HOST = ''
PORT = 50007
server = socket(AF_INET,SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)

conn,addr = server.accept()
print "Contented by: ",addr
while True:
    data = conn.recv(1024)
    if not data:
        break
    print addr, ":", data
    data = raw_input("> ")
    if data == ":q":
        break
    conn.sendall(data)
conn.close()


