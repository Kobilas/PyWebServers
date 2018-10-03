"""
Matthew Kobilas
mk666
CS356-005
"""
from socket import *
from struct import *
from random import *

def serverUDP(servPort):
    servIP = "127.0.0.1"
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind((servIP, servPort))
    while True:
        data, cliAddr = sock.recvfrom(8)
        if randint(1,9) < 4:
            print("Message with sequence number " + str(unpack("II", data)[1]) + " dropped")
            continue
        print("Responding to ping request with sequence number " + str(unpack("II", data)[1]))
        sock.sendto(pack("II", 2, unpack("II", data)[1]), cliAddr)

port = int(input("The server is ready to receive on port: "))
serverUDP(port)
