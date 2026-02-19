import socket

HOST = '127.0.0.1'      # Localhost
                        # None / '' / '0.0.0.0' = All interfaces
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_socket:
    listening_socket.bind((HOST, PORT))
    listening_socket.listen(1)

    message = None
    while message != 'exit':
        print(f'Waiting for connections on {HOST}:{PORT}')
        connection_socket, addr = listening_socket.accept()
        print(f'Accepted connection from {addr[0]}:{addr[1]}')
        with connection_socket:
            while data := connection_socket.recv(4096):
                message = data.decode()
                print(f'Received: {message}')
                if message == 'exit':
                    break
                connection_socket.sendall(data)
        # if message == 'exit':
        #     break
