import socket
import sys

# se crea la conexión
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as error:
    print('Falla al crear la conexion: %s' % error)
    sys.exit(1)

print('Socket creado')
host = 'www.google.cl'
port = 80

# se resuelve el host
try:
    ip_remota = socket.gethostbyname(host)
except socket.gaierror as gerror:
    # no pudo resolver
    print('se produjo un error al resolver el host %s: %s' % (host, gerror))
    sys.exit()


try:
    # conectando
    s.connect((host, port))
    print('conectado al host %s con la ip %s' % (host, ip_remota))
    message = b"GET / HTTP/1.1\nHost: www.google.cl\n\n"
    s.sendall(message)
except Exception as serror:
    print('se produjo un error al enviar el mensaje: %s' % serror)
    sys.exit(2)

print('mensaje enviado con exito')

# obteniendo respuesta de la conexion
reply = s.recv(4096)  # 8192
print(type(reply.decode()))
s.close()

s = 'hola'.encode()
# print(type(s))


