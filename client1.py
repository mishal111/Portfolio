import socket
import threading
import hashlib


Host='127.0.0.1'
port=55555
ID=input("Enter your Nickname:")

socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((Host,port))

def receive():
    try:
       message=socket.recv(1024).decode('ascii')
       if message=="ID":
        socket.send(ID).encode('ascii')
        next_message=socket.recv(1024).decode('ascii')
        if next_message=="PASS":
            with open("PASS.txt","r") as f:
                key=f.read()
            h=hashlib.sha256()
            h.update(key.encode())
            has=h.hexdigest()
            socket.send(has.encode('ascii'))
            if socket.recv(1024).decode('ascii')=="REFUSE":
                print("Incorrect Password\nConnection is refused")
        else:
            print(message)
    
    except:
        print("An error occurred")
        socket.close()