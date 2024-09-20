import socket
from Lab1.test import Coder
import tkinter as tk

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send():
    message = input_text.get("1.0", tk.END).strip()
    client_socket.sendto(message.encode('utf-8'), ("127.0.0.1", 12345))

# code_message = Coder(message)
    # win_message = code_message.utf8_to_windows1251()
    # bin_message = code_message.windows1251_to_bin(win_message)
    # client_socket.sendto(win_message, ("127.0.0.1", 12345))
    # client_socket.sendto(bin_message.encode(), ("127.0.0.1", 12345))

root = tk.Tk()
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)  # Месседжбокс 1
main_frame.grid_columnconfigure(1, weight=0)  # Рамка для кнопок
main_frame.grid_columnconfigure(2, weight=1)  # Месседжбокс 2

input_text = tk.Text(main_frame, height=20, width=40)
input_text.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

button_frame = tk.Frame(main_frame)
button_frame.grid(row=0, column=1, padx=10, pady=5)

output_text = tk.Text(main_frame, height=20, width=40)
output_text.grid(row=0, column=2, padx=10, pady=5, sticky='nsew')

encode_button = tk.Button(button_frame, text="Отправить", width=20, command=send)
encode_button.pack(pady=5)

button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_columnconfigure(0, weight=1)

root.mainloop()
