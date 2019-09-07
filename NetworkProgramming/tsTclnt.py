# TCP client

from socket import *

HOST = '139.159.232.222'
# HOST = '10.201.18.218'
# HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

try:
    while True:
        data = input('> ')
        if not data:
            break
        tcpCliSock.send(bytes(data, 'utf-8'))
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        print(data.decode('utf-8'))
except KeyboardInterrupt:
    pass
finally:
    print("shutting down client...")
    tcpCliSock.close()