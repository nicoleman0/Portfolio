import socket

# Create a server socket object, socket function and specify socket type/family
# AF_INET = IPv4, SOCK_STREAM = TCP
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name and port
host = socket.gethostname()
port = 444

# Bind server socket object the port
serversocket.bind(host, port)

serversocket.listen(3) # TCP listener, 3 clients can queue up

while True:
    # Establish connection with client
    clientsocket, addr = serversocket.accept()
    
    print("Recieved connection from " % str(addr))
    message = 'Hello and thank you for connecting to the server' + "\r\n" # \r\n is the line ending
    clientsocket.send(message)
    
    clientsocket.close