"""
Matthew Kobilas
mk666
CS356-005
"""
from socket import *

# clientUDP from Professor Thomson's socketAPI slides
def clientUDP(servIP, servPort, msg):
    recvd = False
    count = len(msg)
    sock = socket(AF_INET, SOCK_DGRAM)
    print("Client sending data to server " + servIP + ":" + str(servPort) + " -- " + msg + " (" + str(count) + ")")
    sock.sendto(msg.encode(), (servIP, servPort))
    # settimeout() from https://docs.python.org/3/library/socket.html
    for i in range(3):
        sock.settimeout(1)
        while True:
            try:
                ret, servAddr = sock.recvfrom(count)
            except timeout:
                break
            if count > 0:
                print("Client received data from server " + servAddr[0] + ":" + str(servAddr[1]) + " -- " + ret.decode())
                recvd = True
                break
        if recvd:
            break
        if count <= 0:
            break
        print("Message timed out")
    sock.close()

port = int(input("Enter server port number connect to: "))
ip = input("Enter server IP address to connect to: ")
msg = input("Enter message to send: ")
clientUDP(ip, port, msg)
