import socket

# IP address of the receiver
ip_address = "192.168.100.2"

# Port number to use for communication
port = 8000

# Message to send
message = "Hello, world!"

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the receiver's IP address and port
sock.connect((ip_address, port))

# Send the message
sock.sendall(message.encode())

# Close the socket
sock.close()

