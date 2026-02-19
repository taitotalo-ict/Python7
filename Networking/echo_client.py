import socket

HOST = '127.0.0.1'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection_socket:
    connection_socket.connect((HOST, PORT))

    while True:
        message = input('Message (q -> quit): ')
        if message == 'q':
            break
        elif not message:
            continue
        c = connection_socket.sendall(message.encode())
        # print(f'Message lähetetty: {c}')
        data = connection_socket.recv(4096)
        if not data:
            break
        print(f'Received: {data.decode()}')