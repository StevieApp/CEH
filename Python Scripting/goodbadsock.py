#!/bin/python3
#this will show a working socket
import socket
from datetime import datetime as timestamp
import sys

if (len(sys.argv) == 2):
	target = socket.gethostbyname(sys.argv[1])
	print('The ip address is: {}'.format(target))
else:
	print('You need to input the host being scanned')
	print('Syntax: ./semisocket.py <ipaddress/hostname>')
	sys.exit()


print('--'*40)
print('We are trying to scan {} for open ports \n starting at {}'.format(sys.argv[1], timestamp.now()))
print('--'*40)

try:
	for port in range(20,54):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		binarystore = sock.connect_ex((target, port))
		if (binarystore == 0):
			print('Successful connection at port: {}'.format(port))

except KeyboardInterrupt:
	print('Exited by keyboard')

except socket.gaierror:
	print('Could not resolve host')

except socket.error:
	print('Couldn\'t connect to server')
except:
	print('Unknown issue with connection')
