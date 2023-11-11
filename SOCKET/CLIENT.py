import socket
try:
    cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cs.connect((socket.gethostbyname(socket.gethostname()), 12345))

    while True:
        send=input("CLIENT: ")
        cs.send(send.encode())
        msg=cs.recv(1000).decode()
        print('SERVER',msg)
        
except:
    print("NO SERVER AVAILABLE ")
