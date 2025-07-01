import socket
import sys
import time
from scapy.all import *
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((sys.argv[1], int(sys.argv[2])))
data = s.recv(1500)
pkt = IP(data)
pkt.show()

lip = pkt.dst
rip = pkt.src
sport = 20000

def recvlen(length):
    data = b''
    while length > 0:
        tmp = s.recv(length)
        data += tmp
        length -= len(tmp)
    return data

def recvjob():
    while True:
        data = recvlen(20)
        pkt = IP(data)
        length = pkt.len
        datalen = length - 20
        data += recvlen(datalen)
        pkt = IP(data)
        if TCP in pkt and pkt[TCP].flags == "SA":
            print(pkt[TCP].sport)

threading.Thread(target = recvjob).start()

for dport in range(65535):
    pkt = (IP(src=lip, dst=rip) / TCP(sport=sport, dport=dport, flags="S", seq=100))
    s.send(raw(pkt))

time.sleep(1000)



