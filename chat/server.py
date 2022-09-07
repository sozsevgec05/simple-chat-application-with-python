import socket
import time

hostName = "localhost"
portName = 7777

ethernetSocket = socket.socket()
ethernetSocket.bind((hostName, portName))

ethernetSocket.listen(1)

connettion, address = ethernetSocket.accept()

print(str(address) + "The connection is successful.")

while True:
    while True:
        try:
            incomingData = str(connettion.recv(1024).decode())
            print("CLİENT " + incomingData)
            break
        except ConnectionResetError:
            time.sleep(2)
            connettion, address = ethernetSocket.accept()
            print(str(address) + "The connection is successful.")

    if incomingData == "exit":
        break
    else:
        message = input("----- : ")
        print("The client is expected")
        connettion.send(message.encode())

connettion.close()