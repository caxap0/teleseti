import socket
import threading
import tkinter as tk
from test import Coder
from datetime import datetime

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

now = datetime.now()

client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('127.0.0.1', 12345)
client_address = ('127.0.0.1', 12346)

server_socket.bind(server_address)


def message(output_text1, output_text2):
    while True:
        try:
            data, addr = server_socket.recvfrom(1024)
            decoded_message = data.decode('utf-8')

            timing = now.strftime("%d.%m.%Y._%H-%M-%S")

            code_message = Coder(decoded_message)
            win_message = code_message.utf8_to_windows1251()
            hex_encode = ' '.join(f'{byte:02x}' for byte in win_message)
            bin_message = code_message.windows1251_to_bin(win_message)

            output_text1.insert(tk.END, f'{addr}: {decoded_message}\n')
            output_text2.insert(tk.END, f'{addr}\nHex: {hex_encode}\nBin: {bin_message}\n')
            
            with open(f'{timing}.txt', 'a') as file:
                file.write(f"Сообщение от {addr}: {message.decode()}\n")
        except Exception as e:
            output_text1.insert(tk.END, f'Ошибка: {str(e)}\n')
            break


def gui():
    root = tk.Tk()
    main_frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    main_frame.grid_rowconfigure(0, weight=1)
    main_frame.grid_rowconfigure(1, weight=0)
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=1)
    main_frame.grid_columnconfigure(2, weight=0)

    output_text1 = tk.Text(main_frame, height=20, borderwidth=2)
    output_text1.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

    output_text2 = tk.Text(main_frame, height=20, borderwidth=2)
    output_text2.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')

    input_text = tk.Text(main_frame, height=3, borderwidth=2)
    input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

    def send():
        message = input_text.get("1.0", tk.END).strip()

        code_message = Coder(message)
        win_message = code_message.utf8_to_windows1251()
        hex_encode = ' '.join(f'{byte:02x}' for byte in win_message)
        bin_message = code_message.windows1251_to_bin(win_message)

        output_text1.insert(tk.END, f'{server_address}: {message}\n')
        output_text2.insert(tk.END, f'{server_address}\nHex: {hex_encode}\nBin: {bin_message}\n')

        client_socket.sendto(message.encode('utf-8'), client_address)

    send_button = tk.Button(main_frame, text="Отправить", width=20, command=send)
    send_button.grid(row=1, column=2, padx=10, pady=5, sticky='nsew')

    receive_thread = threading.Thread(target=message, args=(output_text1, output_text2))
    receive_thread.daemon = True
    receive_thread.start()

    root.mainloop()


if __name__ == "__main__":
    gui()
