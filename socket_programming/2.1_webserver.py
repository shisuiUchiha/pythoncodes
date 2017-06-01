from socket import *

serverport=13001

serversocket=socket(AF_INET,SOCK_STREAM)
serversocket.bind(('',serverport))

serversocket.listen(1)

print "Ready to receive"

while 1:
	connection_socket,addr=serversocket.accept()
	data=connection_socket.recv(1024).decode('ascii')
	print data[5:14]
	if(data[5:14]=="test.html"):
		connection_socket.send("HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"+"\n")
		connection_socket.send("<html><title>"+"test.html"+"</title></html>\n")
		f=open("test.html","r")
		connection_socket.send(f.read())
		f.close()
		connection_socket.close()
	elif(data[5:14]=="text.html"):
		connection_socket.send("HTTP/1.1 200 OK\n"+"Content-Type: text/html\n"+"\n")
		connection_socket.send("<html><title>"+"text.html"+"</title></html>\n")
		f=open("text.html","r")
		connection_socket.send(f.read())
		f.close()
		connection_socket.close()
	else:
		print "entered"
		connection_socket.send("HTTP/1.1 404 Not Found\n")
		connection_socket.close()


serversocket.close()