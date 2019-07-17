import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # nombre
    nombre = input("nombre:")
    s.sendall(nombre.encode('utf-8') + b'')
    data = s.recv(1024)

    # nick
    nick = input("nick:")
    s.send(nick.encode('utf-8') + b'')
    data = s.recv(1024)

    # mensaje

print('Received', repr(data))