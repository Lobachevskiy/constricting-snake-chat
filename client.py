import socket
import select
import sys

def chat_client():
    import socket # For some reason it doesn't work without it here.
    if(len(sys.argv) < 3) :
        host = 'localhost'
        port = 5594
        #print("Usage : python chat_client.py hostname port")
        #sys.exit()
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.connect((host, port))
        server_socket.settimeout(2)
    except:
        print("Unable to connect.")
        sys.exit()

    print("Connected.")
    sys.stdout.write('[Me] ')
    sys.stdout.flush()

    while True:
        socket_list = [server_socket,]

        ready_to_read, ready_to_write, ready_to_err = \
                       select.select(socket_list, [], [], 0)
        for socket in ready_to_read:
            if socket == server_socket:
                data = socket.recv(1024)
                if data:
                    sys.stdout.write(data.decode())
                    sys.stdout.write('[Me] ')
                    sys.stdout.flush()
                else:
                    print("Disconnected.")
                    sys.exit()
        if sys.stdin.isatty():
            message = sys.stdin.readline()
            server_socket.send(message.encode())
            sys.stdout.write('[Me] ')
            sys.stdout.flush()

if __name__ == "__main__":

    sys.exit(chat_client())
