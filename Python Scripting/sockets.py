#!/bin/python3
#sockets are used to connect two nodes which may either be a connection to an open port or an ip address

import socket

host = '127.0.0.1'
port = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))

#you could decide to keep the port open and send data through it
