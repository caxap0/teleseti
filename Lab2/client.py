import socket
from Lab1.test import Coder

# Настройка клиента (отправителя)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    message = input()
    code_message = Coder(message)
    win_message = code_message.utf8_to_windows1251()
    bin_message = code_message.windows1251_to_bin(win_message)
    client_socket.sendto(win_message, ("127.0.0.1", 12345))
    client_socket.sendto(bin_message.encode(), ("127.0.0.1", 12345))