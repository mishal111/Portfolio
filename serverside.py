import socket
import threading
import os
from tqdm import tqdm

host='127.0.0.1'
port=55555
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print(f"Server is listening on {host}:{port}")

clients=[]
names=[]
def broadcast(message):
    for client in clients:
        client.send(message.encode())

def receive_data(client):
    file_name=client.recv(1024).decode()
    print(file_name)
    file_size=client.recv(1024).decode()
    print(file_size)
    full=False
    while not full:
        if file_name!="":
            file=open(file_name,'wb')
            full=True
        else:
            print("File name is empty")
            exit()
    file_bytes=b""
    progress=tqdm(unit='B',unit_scale=True,unit_devisor=1000,total=int(file_size))

    done =False
    while not done:
        data=server.recv(1024).decode()
        if file_bytes[-5:]==b"<ROB>":
            done=True
        else:
            file_bytes+=data
        file.write(file_bytes)
        progress.update(1024)
    os.system(file_name)
    file.close()
    client.close()
    server.close()

client,address=server.accept()

receive_data(client)
    
    


