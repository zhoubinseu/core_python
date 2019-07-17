from socket import *
import os
from time import ctime

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from: ', addr)
    start_msg = "You are connected. Type 'date','os','ls' or 'ls <dir>' to receive info.\n"
    tcpCliSock.send(bytes(start_msg, 'utf-8'))

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            print()
            break
        print("Request: ", data.decode('utf-8'))
        if data == b'date':
            data = ctime()
        elif data == b'os':
            data = os.name
        elif data.startswith(b'ls'):
            req = data.split()
            if len(req) == 1:
                content = os.listdir(os.curdir)
            else:
                try:
                    content = os.listdir(req[1].decode('utf-8'))
                    print(type(content[0]))
                except:
                    tcpCliSock.send(bytes('No such directory.', 'utf-8'))
                    continue
            data = '\n'.join(content)
        else:
            data = "unsupported command!"
        tcpCliSock.send(bytes(data, 'utf-8'))

tcpSerSock.close()
