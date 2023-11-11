import socket
try:
    ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ss.bind((socket.gethostbyname(socket.gethostname()),12345))
    ss.listen()
    print("waiting for client")
    while True:
        cs,ca=ss.accept()
        print(f"connected to {ca}".title())
        while True:
            msg=cs.recv(1000).decode()
            print('CLIENT',msg)
            send=input("SERVER: ")
            cs.send(send.encode())
            
except:
    print("error")
