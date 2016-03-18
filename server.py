import sys
import socket
import select

HOST = ''
PORT = 5594
SOCKET_LIST = []
BUFF_SIZE = 1024

def chat_server():
    import socket # For some reason it doesn't work without it here.
    main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    main_socket.bind((HOST, PORT))
    print("Chat server is online")
    main_socket.listen(10)

    SOCKET_LIST.append(main_socket)

    while True:
        ready_to_read, ready_to_write, ready_to_err = \
                       select.select(SOCKET_LIST, [], [], 0)

        for socket in ready_to_read:
            if socket == main_socket:
                new_socket, new_socket_addr = main_socket.accept()
                SOCKET_LIST.append(new_socket)
                broadcast("New client connection [%s:%s].\n" % new_socket_addr,
                          main_socket)
            else:
                try:
                    data = socket.recv(BUFF_SIZE)
                    if data:
                        broadcast('[' + str(socket.getpeername()) + '] ' + \
                                  data.decode(),
                                  main_socket, socket)
                    else:
                        if (socket in SOCKET_LIST):
                            SOCKET_LIST.remove(socket)
                            broadcast("Client %s disconnected.\n" %
                                      str(socket.getpeername()),
                                      main_socket)
                except socket.error:
                    broadcast("Client %s disconnected.\n" %
                              str(socket.getpeername()),
                                      main_socket)
                    continue

                
def broadcast(string, server_socket, ignore_socket = None):

    for socket in SOCKET_LIST:
        if socket != ignore_socket:
            if socket == server_socket:
                print(string)
            else:
                try:
                    socket.send(string.encode())
                except socket.error:
                    if socket in SOCKET_LIST:
                        SOCKET_LIST.remove(socket)
                        print("Failed to send")
                    else:
                        print("Failed to send")
if __name__ == "__main__":
    
    sys.exit(chat_server())
