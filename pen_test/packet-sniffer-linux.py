import socket
import os
import sys

# Check for root privileges.
if os.geteuid() != 0:
    print("This script must be run as root!")
    sys.exit(1)

# Create a raw socket and bind it to the public interface
try:
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
except PermissionError as e:
    print("Error: Raw sockets require root privileges.")
    sys.exit(1)

# Infinite loop to receive data from the socket
while True:
    # Receiving all the data from the socket
    # The parameter is the buffer size -> 65565 bytes is maximum
    packet, addr = serversocket.recvfrom(65565)
    print(f"Packet from {addr}: {packet.hex()}") # print the packet data in hexadecimal format
