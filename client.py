import socket
import os

sender=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sender.connect(('127.0.0.1',5555))

file=open("The.Social.Network.2010.1080p.BluRay.x265-RARBG.srt","rb")
file_size=os.path.getsize('The.Social.Network.2010.1080p.BluRay.x265-RARBG.srt')

sender.send("recieved_file.srt".encode())
sender.send(srt(file_size).encode())

data=file.read()
sender.sendall(data)
sender.send(b"<END>")
