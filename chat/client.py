import socket
import time

hostName = "localhost"
portName = 7777

ethernetSocket = socket.socket()
ethernetSocket.connect((hostName, portName))

print("Connection is provided!!! {}:{}".format(hostName, portName)) 

message = input("----- : :")
print("The server is expected")

while message != "exit":
    ethernetSocket.send(message.encode())
    incomingData = ethernetSocket.recv(1024).decode()

    print("SERVER: " + incomingData)

    message = input("----- : ")
    print("The server is expected")

ethernetSocket.close()