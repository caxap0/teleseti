import socket
import tkinter as tk
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("127.0.0.1", 12345))


def message():
    while True:
        output_text.delete(tk.END)
        message, address = server_socket.recvfrom(1024)
        output_text.insert("1.0", f'Вам пришло сообщение от {address}: \n{message.decode()}')
        with open('save.txt', 'a') as file:
            file.write(f"Сообщение от {address}: {message.decode()}\n")

def treads():
    tread = threading.Thread(target=message)
    tread.start()


root = tk.Tk()
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

main_frame.grid_rowconfigure(0, weight=1)
main_frame.grid_columnconfigure(0, weight=1)

output_text = tk.Text(main_frame, height=20, borderwidth=2)
output_text.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

treads()

root.mainloop()



