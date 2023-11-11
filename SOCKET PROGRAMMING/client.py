import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address=host,port=( socket.gethostbyname(socket.gethostname()), 12347)
client.connect(address)

msg=client.send("client".encode('utf-8'))
recv=client.recv(1000).decode('utf-8')


print(msg)

