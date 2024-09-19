import socket
from Lab1.test import Coder

# Настройка клиента (отправителя)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input()
    code_message = Coder.utf8_to_windows1251(message)
    client_socket.sendto(code_message, ("127.0.0.1", 12345))