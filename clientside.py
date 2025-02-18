import socket
import tqdm
import os

host='127.0.0.1'
port=55555
socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.connect((host,port))

def send_data():
    try:
        sendfile=input("Enter the name of the file with the extension:")
        file=open(sendfile,'rb')
        socket.send(sendfile.encode())
        file_size=os.path.getsize(sendfile)
        socket.send(str(file_size).encode())
        
        data=file.read()
        socket.sendall(data)
        socket.send(b"<ROB>")

    except FileNotFoundError:
        print(f"{sendfile} is not found in the directory")
    

    socket.close()

send_data()



