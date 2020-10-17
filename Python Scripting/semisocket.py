#!/bin/python3
#new portscanner with issues though
#it checks through a specific ip range to check whether a port is open

import socket
import sys
from datetime import datetime as timestamp

#first, we check that there are only two arguments
if len(sys.argv) == 2:
	#allows for the use of a hostname instead of an ip address
	target = socket.gethostbyname(sys.argv[1])
	print('{} this hostname is {}'.format(sys.argv[1], target))
else :
	print('input one variable/argument')
	print('Syntax: ./semisocket.py <ipaddress/hostname>')
	sys.exit()

def newline():
	print('\n')

#creating a banner to show that progress is happening
print('--'*40)
print('Scanning ip: {} starting at {}'.format(sys.argv[1], timestamp.now()))
print('Waiting...')
print('--'*40)
newline()

host = target
port = 9090

#REASONS THE PORTSCANNER MAY END UP HAVING ISSUES
#threading could have been used to make the process faster
#if the ip is not resolvable,,, what happens?? there is no way to make sure that it catches such issues

try:	
	for port in range(1,65535):
		socks = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		#sets a timeout for connection in case it does not happen
		socket.setdefaulttimeout(1)
		
		#we do not use this since an exception will occur and an exception will be thrown
		#socks.connect((host, port))

		#we use the connection with an exception checker which is a '0' with success and '1' without success
		storing = socks.connect_ex((host, port)) 
		if(storing == 0):
			print('Successful connection at port: {}'.format(port))
			newline()

#for keyboard interruptions
except KeyboardInterrupt:
	print('Keyboard Pressed... Exiting now')
	sys.exit()
#dns issue
except socket.gaierror:
	print('Hostname could not be resolved')
	sys.exit()

except socket.error:
	print('Couldn\'t connect to server')

except:
	print('There was an unspecified issue with connection')
	newline()

