import socket

socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket.bind(('172.0.0.1',5555))
socket.listen()

sender,address=socket.accept()

file_name=sender.recv(1024).decode()
print(file_name)
file_size=sender.recv(1024).decode()
print(file_size)

f=open(file_name,"wb")

file_bytes=b""
done=False
progress=tqdm.tqdm(unit='B',unit_scale=True,unit_devisor=1000,total=int(file_size))

while not done:
    data=sender.recv(1024).decode()
    if file_bytes[-5:]==b"<END>":
        done=True
    else:
        file_bytes+=data
    progress.update(1024)

f.write(file_bytes)
f.close()
sender.close()
socket.close()
