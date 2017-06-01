import random
from socket import *

socketport=12000
socketserver=socket(AF_INET,SOCK_DGRAM)

socketserver.bind(('',socketport))

print "Server is up and running"

while True:
	rand = random.randint(0,10)
	message, address = socketserver.recvfrom(1024)
	message = message.upper()
	if rand < 4:
		continue
	socketserver.sendto(message, address)



