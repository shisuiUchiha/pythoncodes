from socket import *

socketport=12000
socketserver=socket(AF_INET,SOCK_DGRAM)

socketserver.bind(('',socketport))

x=0
while 1:
	if(x==0):
		print "server is listening"
		x=x+1
	message,clientaddress=socketserver.recvfrom(2048)
	modified_message=message.upper()
	socketserver.sendto(modified_message,clientaddress)

socketserver.close()
