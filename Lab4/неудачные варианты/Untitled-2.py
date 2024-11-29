from socket import *
import tkinter as tk
import threading
from test import Coder
import pickle

class Message:
    def __init__(self, content):
        self.content = content

    def serialize(self):
        return pickle.dumps(self)

    @staticmethod
    def deserialize(serialized_message):
        return pickle.loads(serialized_message)

class UDP:
    def __init__(self, ip_port):
        self.ip_port = ip_port

    def server_up(self):
        server_socket = socket(AF_INET, SOCK_DGRAM)
        server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_socket.bind(self.ip_port)
        print('UDP сервер запущен и ожидает сообщений...')
        # ПРИНИМАЕМ СООБЩЕНИЕ
        while True:
            data, addr = server_socket.recvfrom(1024)
            message = Message.deserialize(data).content

            formatted_message = f'{addr}: {message}\n'
            self.output_text1.insert(tk.END, formatted_message)

            code_message = Coder(message)
            win_message = code_message.utf8_to_windows1251()
            hex_encode = ' '.join(f'{byte:02x}' for byte in win_message)
            bin_message = code_message.windows1251_to_bin(win_message)
            self.output_text2.insert(tk.END, f'{addr}:\nHex: {hex_encode}\nBin: {bin_message}\n')
    
    # ОТПРАВЛЯЕМ СООБЩЕНИЕ
    def send_message(self):
        message = Message(self.input_text.get('1.0', tk.END).strip())
        
        ser_message = message.serialize()
        deser_message = Message.deserialize(ser_message).content

        client_ip = (self.client_ip_entry.get().strip(), 12345)

        client_socket = socket(AF_INET, SOCK_DGRAM)
        client_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        client_socket.sendto(ser_message, client_ip)

        formatted_message = f'{self.ip_port}: {deser_message}\n'
        self.output_text1.insert(tk.END, formatted_message)

        code_message = Coder(deser_message)
        win_message = code_message.utf8_to_windows1251()
        hex_encode = ' '.join(f'{byte:02x}' for byte in win_message)
        bin_message = code_message.windows1251_to_bin(win_message)
        self.output_text2.insert(tk.END, f'{self.ip_port}:\nHex: {hex_encode}\nBin: {bin_message}\n')


        client_socket.close()
        self.input_text.delete('1.0', tk.END)

    def start_server_thread(self):
        server_thread = threading.Thread(target=self.server_up)
        server_thread.daemon = True
        server_thread.start()

    def gui(self):
        root = tk.Tk()
        main_frame = tk.Frame(root)
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=0)
        main_frame.grid_rowconfigure(2, weight=0)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_columnconfigure(2, weight=0)

        self.output_text1 = tk.Text(main_frame, height=20, borderwidth=2)
        self.output_text1.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

        self.output_text2 = tk.Text(main_frame, height=20, borderwidth=2)
        self.output_text2.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')

        self.input_text = tk.Text(main_frame, height=3, borderwidth=2)
        self.input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        self.client_ip_entry = tk.Entry(main_frame, width=15)
        self.client_ip_entry.grid(row=4, column=1, padx=5, pady=5, sticky='w')

        start_button = tk.Button(main_frame, text="Запустить", width=20, command=self.start_server_thread)
        start_button.grid(row=3, column=1, padx=10, pady=5, sticky='nsew')

        send_button = tk.Button(main_frame, text="Отправить", width=20, command=self.send_message)
        send_button.grid(row=1, column=2, padx=10, pady=5, sticky='nsew')

        root.mainloop()


r = UDP(('127.0.0.1', 12346))
# local_hostname = gethostname()
# server_ip = gethostbyname_ex(local_hostname)[2][0]
# r = UPD(server_ip, 12345)
r.gui()
