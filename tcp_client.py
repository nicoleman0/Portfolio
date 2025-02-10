import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444 # Arbitrary port, but it must match the server's port

clientsocket.connect((host, port)) # Connect to the server

message = clientsocket.recv(1024) # 1024 refers to bytes of data to be received

clientsocket.close()

print(message.decode('ascii')) # Decode the message and print it