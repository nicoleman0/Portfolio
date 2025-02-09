import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444

clientsocket.connect(host, port) # Connect to the server

message = clientsocket.recv(1024) # Receive data from the server

clientsocket.close()

print(message.decode('ascii')) # Decode the message and print it