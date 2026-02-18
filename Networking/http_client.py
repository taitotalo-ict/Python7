import socket

# Valmista socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'httptest.nube.fi'
PORT = 80

s.connect((HOST, PORT))

# Lähettää HTTP pyyntö
# CR = '\r'
# LF = '\n'
http_request = f'GET / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n'
s.send(http_request.encode())

# Vastaanottaa HTTP vastaus
response = b''
while data := s.recv(4096):
    response += data

# Sulkea yhteys
s.close()

header, body = response.split(b'\r\n\r\n')
header = header.decode('ascii')
# Saada otsikot dict:nä
headers = {k:v for row in header.split('\r\n')[1:] for k,v in [row.split(': ')]}

print('### HEADER ###')
print(header, '\n')

print('### BODY ###')
if headers['Content-Type'].startswith('text') or headers['Content-Type'] == 'image/svg+xml':
    print(body.decode('utf-8'))
else:
    print('[Binary content]')

# with open('python.png', 'wb') as file:
#     file.write(body)