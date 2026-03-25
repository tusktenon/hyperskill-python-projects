import socket

# HOST = '127.0.0.1'
HOST = '0.0.0.0'
PORT = 6379

with socket.socket() as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    while True:
        conn, addr = server_socket.accept()
        with conn:
            while data := conn.recv(1024):
                match data.decode():
                    case '+PING\r\n':
                        conn.send(b'+PONG\r\n')
                    case '+EXIT\r\n':
                        exit(0)
                    case _:
                        conn.send(b'-Unknown command!\r\n')
