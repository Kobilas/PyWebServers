"""
Matthew Kobilas
mk666
CS356-005
"""
from socket import *
from time import *
from struct import *
from random import *

def clientUDP(servIP, servPort):
    pcktsSent = 0
    pcktsRcvd = 0
    rtts = []
    sock = socket(AF_INET, SOCK_DGRAM)
    print("Pinging " + servIP + ":" + str(servPort) + " --")
    for i in range(10):
        sock.settimeout(None)
        sent = clock()
        sock.sendto(pack("II",1,i+1), (servIP, servPort))
        pcktsSent += 1
        #sleep(randint(0,4))
        sock.settimeout(1)
        while True:
            try:
                ret, servAddr = sock.recvfrom(8)
            except timeout:
                print("Ping message number " + str(i+1) + " timed out")
                break
            if ret is not None:
                recvd = clock()
                print("Ping message number " + str(i+1) + " RTT: %.6f secs" % (recvd-sent))
                pcktsRcvd += 1
                rtts.append(recvd-sent)
                break
    sock.close()
    print("Packets sent: " + str(pcktsSent))
    print("Packets recieved: " + str(pcktsRcvd))
    print("Packets lost: " + str(pcktsSent-pcktsRcvd))
    print("Packet loss rate: %.6f%%" % ((1-pcktsRcvd/pcktsSent)*100)) 
    minRtt = rtts[0]
    maxRtt = rtts[0]
    avgRtt = 0
    for trip in rtts:
        if trip < minRtt:
            minRtt = trip
        if trip > maxRtt:
            maxRtt = trip
        avgRtt += trip
    avgRtt = avgRtt/pcktsRcvd
    print("Minimum RTT: %.6f secs" % minRtt)
    print("Maximum RTT: %.6f secs" % maxRtt)
    print("Average RTT: %.6f secs" % avgRtt)

port = int(input("Enter server port number connect to: "))
ip = input("Enter server IP address to connect to: ")
clientUDP(ip, port)
