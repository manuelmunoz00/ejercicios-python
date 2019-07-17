import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to the port
server_address = ('127.0.0.1', 65432)
print('starting up on {} port {}'.format(*server_address))  #son 2 elementos, separo tupla
sock.bind(server_address)

# Listen for incoming connections
sock.listen()
# sock.setblocking(0)

"""
Diccionario para almacenar los usuarios (nick,nombre)
ejemplo: usuarios = {'nick': string, 'nombre': string}
"""
usuarios = {}

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)  # a lo mas 16 bits
            print('received {!r}'.format(data))
            if data:
                # data_recibida = format(data)
                data_str = data.decode('utf-8')
                protocolo_nombre = 'n:'
                protocolo_nick = 'k:'
                nombre = ''
                nick = ''

                if protocolo_nombre in data_str:
                    # print(type(data_str))
                    # print(len(data_str))
                    # print(data_str[2:])
                    nombre = data_str[2:]

                if protocolo_nick in data_str:
                    nick = data_str[2:]

                usuarios[nick] = [nombre, nick]

                print(usuarios)


                # print('data_recibida'+ data_recibida)
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no data from', client_address)
                break
            #se libera cuando es "none" o "vacio"
    finally:
        # Clean up the connection
        connection.close()