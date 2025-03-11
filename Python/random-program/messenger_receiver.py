import socket

# Set up the socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set the IP address and port to listen on
ip_address = "192.168.100.2" # Replace with the IP address of the other device
port = 8000 # Replace with the port number to listen on

# Bind the socket to the IP address and port
sock.bind((ip_address, port))

# Listen for incoming connections
sock.listen()

print(f"Listening for incoming connections on {ip_address}:{port}...")

# Accept incoming connections and receive messages
while True:
    conn, addr = sock.accept()
    print(f"Received connection from {addr[0]}:{addr[1]}")
    data = conn.recv(1024)
    if not data:
        break
    message = data.decode()
    print(f"Received message: {message}")
    conn.close()
