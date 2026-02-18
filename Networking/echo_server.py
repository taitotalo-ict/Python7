import socket

HOST = '127.0.0.1'      # Localhost
                        # None / '' / '0.0.0.0' = All interfaces
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print(f'Accepted connection from {addr}')
    with conn:
        data = conn.recv(4096)
        print(data.decode())
        conn.send(data)

