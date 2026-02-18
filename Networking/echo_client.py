import socket

HOST = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'Hello world')
    data = s.recv(4096)

print(f'Received: {data.decode()}')