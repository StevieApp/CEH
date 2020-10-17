#!/bin/python3
import sys
import socket

host = '127.0.0.1'
port = 9090

socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socks.connect((host,port))
