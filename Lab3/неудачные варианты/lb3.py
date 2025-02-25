import socket
import threading
import tkinter as tk
from test import Coder
from datetime import datetime

client_socket = None
server_socket = None

now = datetime.now()


def receive_message(output_text1, output_text2):
    global server_socket
    while True:
        try:
            client_conn, addr = server_socket.accept()
            data = client_conn.recv(1024)
            decoded_message = data.decode('utf-8')

            timing = now.strftime("%d.%m.%Y._%H-%M-%S")

            code_message = Coder(decoded_message)
            win_message = code_message.utf8_to_windows1251()
            hex_encode = ' '.join(f'{byte:02x}' for byte in win_message)
            bin_message = code_message.windows1251_to_bin(win_message)

            output_text1.insert(tk.END, f'{addr}: {decoded_message}\n')
            output_text2.insert(tk.END, f'{addr}\nHex: {hex_encode}\nBin: {bin_message}\n')

            with open(f'{timing}.txt', 'a') as file:
                file.write(f"Сообщение от {addr}: {decoded_message}\n")
        except Exception as e:
            print(f'Ошибка: {str(e)}')


def gui():
    root = tk.Tk()
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=0)
    main_frame.grid_rowconfigure(2, weight=0)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_columnconfigure(2, weight=0)

    output_text1 = tk.Text(main_frame, height=20, borderwidth=2)
    output_text1.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

    output_text2 = tk.Text(main_frame, height=20, borderwidth=2)
    output_text2.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')

    input_text = tk.Text(main_frame, height=3, borderwidth=2)
    input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

    client_ip_entry = tk.Entry(main_frame, width=15)
    client_ip_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

    def connect():
        global server_address, client_address, server_socket, client_socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # local_hostname = socket.gethostname()

        # server_ip = socket.gethostbyname_ex(local_hostname)[2][0]
        server_ip = '127.0.0.1'
        client_ip = client_ip_entry.get().strip()

        server_address = (server_ip, 12346)
        client_address = (client_ip, 12345)

        server_socket.bind(server_address)
        server_socket.listen(5)

        client_socket.connect(server_address)

    def send_message():
        global server_adress
        message = input_text.get("1.0", tk.END).strip()

        code_message = Coder(message)
        win_message = code_message.utf8_to_windows1251()
        hex_encode = ' '.join(f'{byte:02x}' for byte in win_message)
        bin_message = code_message.windows1251_to_bin(win_message)

        output_text1.insert(tk.END, f'{server_address}: {message}\n')
        output_text2.insert(tk.END, f'{server_address}\nHex: {hex_encode}\nBin: {bin_message}\n')

        client_socket.send(message.encode('utf-8'))

        receive_thread = threading.Thread(target=receive_message, args=(output_text1, output_text2))
        receive_thread.daemon = True
        receive_thread.start()

    send_button = tk.Button(main_frame, text="Отправить", width=20, command=send_message)
    send_button.grid(row=1, column=2, padx=10, pady=5, sticky='nsew')

    connect_button = tk.Button(main_frame, text="Подключить", width=20, command=connect)
    connect_button.grid(row=3, column=2, padx=10, pady=5, sticky='nsew')

    root.mainloop()


if __name__ == "__main__":
    gui()
