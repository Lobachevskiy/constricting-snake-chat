import socket
import select
import sys
import textinput

class ChatClient:
    def __init__(self):
        self.server_socket = None
        self.on_received = None
        self.message = ''

    def connect(self, host = 'localhost', port = 5594):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.server_socket.connect((host, port))
            print("Connected.")
        except:
            print("Unable to connect.")
            sys.exit()
    
    def receive(self):
        socket_list = [self.server_socket,]

        ready_to_read, ready_to_write, ready_to_err = \
                       select.select(socket_list, [], [], 0)
        for socket in ready_to_read:
            if socket == self.server_socket:
                data = socket.recv(1024)
                if data:
                    self.message = data.decode()
                    self.on_received()
                    #Send it to frontend
                    print(data.decode())
                else:
                    print("Disconnected.")
                    sys.exit()

    def send_message(self, message):
        self.server_socket.send(message.encode())
