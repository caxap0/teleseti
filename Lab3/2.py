from socket import *
import threading
import tkinter as tk

IP = gethostbyname(gethostname)
PORT = 5000

class Socket:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.conn = None
        self.addr = None
    
    def server_bind(self):
        self.socket.bind((IP, PORT))
        self.socket.listen(1)
        self.conn, self.addr = self.socket.accept()
    
    def client_bind(self):
        self.socket.connect(self.addr)

    def send(self, message):
        self.conn.send(message.encode())

    def recv(self):
        return self.conn.recv(1024).decode()

    def close(self):
        self.socket.close()

class GUI:
    def __init__(self):
        self.socket = Socket()
        self.port = 5001
        self.root = tk.Tk()
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=0)
        self.main_frame.grid_rowconfigure(2, weight=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(2, weight=0)

        self.output_text1 = tk.Text(self.main_frame, height=20, borderwidth=2)
        self.output_text1.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

        self.output_text2 = tk.Text(self.main_frame, height=20, borderwidth=2)
        self.output_text2.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')

        self.input_text = tk.Text(self.main_frame, height=3, borderwidth=2)
        self.input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

        self.client_ip_entry = tk.Entry(self.main_frame, width=15)
        self.client_ip_entry.grid(row=3, column=1, padx=5, pady=5, sticky='w')

        self.send_button = tk.Button(self.main_frame, text="Отправить", width=20, command=self.send_message)
        self.send_button.grid(row=1, column=2, padx=10, pady=5, sticky='nsew')

        self.connect_button = tk.Button(self.main_frame, text="Подключить", width=20, command=self.connect)
        self.connect_button.grid(row=3, column=2, padx=10, pady=5, sticky='nsew')

        self.root.mainloop()
    
    def connect(self):
        client_ip = self.client_ip_entry.get().strip()
        self.socket.bind(client_ip, self.port)
    
    def send_message(self):
        pass


def main():
    g = GUI()