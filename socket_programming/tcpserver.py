from socket import *

serverport=12000

socket_server=socket(AF_INET,SOCK_STREAM)

socket_server.bind(('',serverport))

socket_server.listen(1)

print "ready to receive the data"
x=0

while 1:
	connection_socket,addr=socket_server.accept()
	if(x==0):
		print connection_socket
		print addr
		x=x+1
	sentence=connection_socket.recv(1024)
	modified_sentence=sentence.upper()
	connection_socket.send(modified_sentence)
	connection_socket.close()
