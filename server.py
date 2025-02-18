import socket

HOST='127.0.0.1'
PORT=9090

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(5)
print(f"Server is listening on {HOST}:{PORT}")

while True:
    communication_socket,address=server.accept()
    print(f"The connection with {address} is successful")
    message=communication_socket.recv(1024).decode('utf-8')
    print(f"Message is from client: {message}")
    communication_socket.send("The message recived sucessfully".encode('utf-8'))    
    communication_socket.close()