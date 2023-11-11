import socket

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address=host,port=(socket.gethostbyname(socket.gethostname()),12347)
print(host)
server.bind(address)

server.listen()

while True:
    cs,ca=server.accept()
    
    print(cs)
    print(ca)
    
    csmsg=cs.recv(1024).decode('utf-8')
    
    print(csmsg)
    
    cs.send("server".encode('utf-8'))
    
    cs.close()
