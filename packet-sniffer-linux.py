import socket

# Creating a raw socket, using family=AF_INET and type=SOCK_RAW
# AF_INET is the address family for IPv4, and SOCK_RAW is the socket type for raw packets, IPPROTO_TCP is the protocol number for TCP packets
serversocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# Infinite loop to recieve data from the socket
while True:
    print(serversocket.recvfrom(65565)) # recieving all the data from the socket, parameter is the buffer size -> 65565 bytes is maximum
