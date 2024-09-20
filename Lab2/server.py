import socket

# Настройка сервера (получателя)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 12345))

print("Сервер ожидает сообщения...")

# Ожидание сообщения
while True:
    message, address = server_socket.recvfrom(1024)  # 1024 - размер буфера
    print(f"Сообщение от {address}: {message.decode()}")
