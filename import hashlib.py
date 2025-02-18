import socket
import threading
import hashlib

Host='127.0.0.1'
port=55555
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((Host,port))
print(f"Server is listening on {Host}:{port}")
users=[]
IDs=[]

def broadcast(message):
    for user in users:
        user.send(message.encode('ascii'))

def handle(user):
    while True:
        try:
            message=user.recv(1024).decode('ascii')
            broadcast(message)
        except:
            user_index=users.index(user)
            users.remove(user_index)
            IDs.remove(user_index)
            user.send("An error occuerrd".encode('ascii'))
            broadcast(f"{IDs.index(user_index) } is left the chat")
            user.close()



def receive():
    while True:
        user,address=server.accept()
        user.send("NICK".encode('ascii'))
        ID=user.recv(1024).decode('ascii')
        if ID=='admin':
            user.send("PASS".encode('ascii'))
            with open("PASS,txt","r") as f:
                key=f.read()
            h=hashlib.sha256()
            h.update(key.encode())
            has=h.hexdigest()
            password=message.recv(1024).decode('ascii')
            if key!=password:
                user.send("REFUSE".encode('ascii'))
                user.close()

        users.append(user)
        IDs.append(ID)
        user.send("Connected to the server".encode('ascii'))
        broadcast(f"{ID} is joined the chat")
        thread=threading.Thread(target=handle,args=user)
        thread.start()

receive()