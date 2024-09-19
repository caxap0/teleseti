import socket

# Настройка клиента (отправителя)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input()  # Сообщение для отправки
    client_socket.sendto(message.encode(), ("127.0.0.1", 12345))