import socket
ss=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((socket.gethostbyname(socket.gethostname()), 12345))
ss.listen(1000)
print("waiting for client connection...".title())
while True:
    
    cs,ca= ss.accept()
    print(f"{ca} Connected")
    while True:
        recieve=cs.recv(10000).decode('utf-8')
        print(f"CLIENT: {recieve}")
        send=input("SERVER: ").encode()
        cs.send(send)
    
    
