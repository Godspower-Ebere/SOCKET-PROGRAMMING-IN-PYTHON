import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12346)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

while True:
    #print('Waiting for a client connection...')
    client_socket, client_address = server_socket.accept()
    print('Connected to:', client_address)

    # Receive data from the client
    data = client_socket.recv(1000000000000000000000000000000000)
    if data:
        print('Received:', data.decode())

    # Send a response back to the client
    response = input("SERVER: ")
    client_socket.send(response.encode())

    # Close the connection
    client_socket.close()
