from socket import *

HOST = input('Enter host: ')
if not HOST:
    HOST = 'localhost'
PORT  = input('Enter port: ')
if not PORT:
    PORT = 21567

BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

data = tcpCliSock.recv(BUFSIZ)
print(data.decode('utf-8'))

while True:
    data = input("> ")
    if not data:
        break
    tcpCliSock.send(bytes(data,'utf-8'))
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode('utf-8'))

tcpCliSock.close()