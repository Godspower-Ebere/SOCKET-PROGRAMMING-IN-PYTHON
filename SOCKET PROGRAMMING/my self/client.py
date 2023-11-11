import socket
try:
    cs=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cs.connect((socket.gethostbyname(socket.gethostname()), 12345))
    
    while True:
        send=input("CLIENT: ").strip().encode()
        cs.send(send)
            
        receive=cs.recv(10000).decode()
        print(f"SERVER: {receive}")
    
except:
    print("NO AVAILABLE SERVER")
