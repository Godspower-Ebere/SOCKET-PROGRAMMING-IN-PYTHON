import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12346)
client_socket.connect(server_address)

# Send data to the server
message = input("CLIENT: ")
client_socket.send(message.encode())

# Receive the server's response
response = client_socket.recv(1024)
if response:
    print('Received:', response.decode())

# Close the connection
client_socket.close()
