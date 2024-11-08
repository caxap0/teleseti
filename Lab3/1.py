import socket
from socket import *
import tkinter as tk
import threading

IP = gethostbyname(gethostname())
PORT = 5000


class Socket:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)

    def load(self, ip, port):
        self.ip = ip
        self.port = port

    def bind(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
        threading.Thread(target=self.recv).start()

    def send(self, text):
        if self.conn:
            self.conn.send(text.encode('utf-8'))

    def recv(self):
        while True:
            data = self.conn.recv(1024)
            if data:
                decoded_data = data.decode('utf-8')
                gui.display_message(decoded_data)


class GUI:
    def __init__(self):
        self.socket = Socket()
        self.ip = IP
        self.port = PORT

    def connect(self):
        client_ip = self.client_ip_entry.get().strip()
        self.socket.load(client_ip, self.port)
        threading.Thread(target=self.socket.bind).start()

    def send_message(self):
        message = self.input_text.get("1.0", tk.END).strip()
        if message:
            self.output_text1.insert(tk.END, f'You: {message}\n')
            self.socket.send(message)
            self.input_text.delete("1.0", tk.END)

    def display_message(self, message):
        self.output_text2.insert(tk.END, f'Client: {message}\n')

    def interface(self):
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
        self.client_ip_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.send_button = tk.Button(main_frame, text="Отправить", width=20, command=self.send_message)
        self.send_button.grid(row=1, column=2, padx=10, pady=5, sticky='nsew')

        self.connect_button = tk.Button(main_frame, text="Подключить", width=20, command=self.connect)
        self.connect_button.grid(row=3, column=2, padx=10, pady=5, sticky='nsew')

        root.mainloop()


if __name__ == "__main__":
    gui = GUI()
    gui.interface()
