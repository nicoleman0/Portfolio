from scapy.all import sr1
from scapy.layers.inet import IP, TCP
from scapy.layers.inet import TCP
import socket

ip = IP(dst=socket.gethostbyname("www.example.com"))
syn = TCP(dport=80, flags="S") # S flag indicates a SYN packet
pkt = ip/syn # Construct the complete TCP SYN packet
response = sr1(pkt, timeout=1)
response = sr1(pkt, timeout = 1)

if response: 
    response.show() 
else: 
    print("No response received") 