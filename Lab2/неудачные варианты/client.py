import socket
from teleseti.Lab1.test import Coder
import tkinter as tk

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


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
        output_text1.delete("1.0", tk.END)
        output_text2.delete("1.0", tk.END)
        output_text1.insert("1.0", f'Вы отправили сообщение: {message}')
        output_text2.insert("1.0", hex_encode + '\n')
        output_text2.insert("2.0", bin_message)

        client_message = f'{message}\n{hex_encode}\n{bin_message}'
        client_socket.sendto(client_message.encode('utf-8'), ("127.0.0.1", 12345))

    send_button = tk.Button(main_frame, text="Отправить", width=20, command=send)
    send_button.grid(row=1, column=2, padx=10, pady=5, sticky='nsew')

    root.mainloop()


if __name__ == "__main__":
    gui()
