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

pkt = (IP(src=lip, dst=rip) / ICMP(type="echo-request"))
pkt.show()
s.send(raw(pkt))

data = s.recv(1500)
pkt = IP(data)
pkt.show()


