from socket import *
import sys

addr = ('127.0.0.1', 12345)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect(addr)

while True:
    data = input('Сообщение: ')
    if not data:
        tcp_socket.close()
        sys.exit(1)

    data = str.encode(data)
    tcp_socket.send(data)
    data = bytes.decode(data)
    data = tcp_socket.recv(1024)
    print(data)


    tcp_socket.close()