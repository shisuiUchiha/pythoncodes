from socket import *

serverip='127.0.0.1'
serverport=12000


socketclient=socket(AF_INET,SOCK_DGRAM)

#AF_INET means we ar using ipv4 in network layer
#SOCK_DGRAM means we are using UDP in transport layer

message=raw_input("enter something in lowercase letters-")
socketclient.sendto(message,(serverip,serverport))

receivedmessage,serveraddress=socketclient.recvfrom(2048)

print receivedmessage
print serveraddress

socketclient.close()