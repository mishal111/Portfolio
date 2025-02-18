import socket
import threading

HOST='127.0.0.1'
PORT=55555

serverr=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverr.bind((HOST,PORT))
serverr.listen()
print(f"Server is listening on {HOST}:{PORT}")

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message.encode('ascii'))
def handle(client):
    while True:
        try:
            message=client.recv(1024).decode('ascii')
            broadcast(message)
        except:
            clientIndex=clients.index(client)
            clients.pop(clientIndex)
            nickname=nicknames.index[clientIndex]
            nicknames.pop(clientIndex)
            nicknames.close()
            broadcast(f"{nickname} left the chat")
            client.close()
            break

def receive():
    while True:
        client,address = serverr.accept()
        print(f"Connected with {address}")

        client.send("NICK".encode('ascii'))
        nickname=client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)
        broadcast(f"{nickname} is joined the chat")
        client.send("Connected to the server".encode('ascii'))

        thread=threading.Thread(target=handle,args=(client,))
        thread.start()