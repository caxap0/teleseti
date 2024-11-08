from socket import *

tcp_socket = socket(AF_INET, SOCK_STREAM)

tcp_socket.bind(('127.0.0.1', 12345))
tcp_socket.listen(1)

while True:
    print('wait connection...')

    conn, addr = tcp_socket.accept()
    print('client_addr:', addr)

    data = conn.recv(1024)
    
    if not data:
        conn.close()
        break
    else:
        print(data)
        conn.send(b'Hello from server!')
    
tcp_socket.close()
