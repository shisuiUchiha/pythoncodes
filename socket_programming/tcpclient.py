from socket import *

serverip='127.0.0.1'
serverport=12000

socket_client=socket(AF_INET,SOCK_STREAM)
socket_client.connect((serverip,serverport))


sentence=raw_input("enter a lower case sentence-")

socket_client.send(sentence)

modified_sentence=socket_client.recv(1024)

print modified_sentence
print socket_client

socket_client.close()
