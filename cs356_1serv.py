"""
Matthew Kobilas
mk666
CS356-005
"""
from socket import *

# serverUDP from Professor Thomson's socketAPI slides
def serverUDP(servPort):
    servIP = "127.0.0.1"
    dataLen = 100
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((servIP, servPort))
    print("The server is ready to receive on port: " + str(servPort))
    while True:
        data, cliAddr = sock.recvfrom(dataLen)
        print("Server received data from client " + cliAddr[0] + ":" + str(servPort) + " -- " + data.decode())
        print("Server sending data to client " + cliAddr[0] + ":" + str(servPort) + " -- " + data.decode())
        sock.sendto(data, cliAddr)

port = int(input("Enter port number to run server on that port: "))
serverUDP(port)
