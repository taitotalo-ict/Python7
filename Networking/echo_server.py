import socket
from threading import Thread

HOST = '127.0.0.1'      # Localhost
                        # None / '' / '0.0.0.0' = All interfaces
PORT = 1234
stop_signal = False


def handle_connection(connection_socket):
    global stop_signal
    with connection_socket:
        while not stop_signal:
            try:
                data = connection_socket.recv(4096)
            except socket.timeout:
                continue
            if not data:
                break
            message = data.decode()
            print(f'Received: {message}')
            if message == 'exit':
                print('Exit signal received.')
                stop_signal = True
                break
            connection_socket.sendall(data)
    print('Terminating thread.')


socket.setdefaulttimeout(0.3)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_socket:
    listening_socket.bind((HOST, PORT))
    listening_socket.listen(1)

    while not stop_signal:
        print(f'Waiting for connections on {HOST}:{PORT}')
        try:
            connection_socket, addr = listening_socket.accept()
        except socket.timeout:
            continue
        print(f'Accepted connection from {addr[0]}:{addr[1]}')
        Thread(target=handle_connection, args=(connection_socket,)).start()

print('Exiting main thread')