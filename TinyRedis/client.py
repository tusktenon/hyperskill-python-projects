import socket

HOST = '127.0.0.1'
PORT = 6379

with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        print('1. Send PING\n2. Send EXIT\n3. Exit client')
        match input():
            case '1':
                client_socket.send('+PING\r\n'.encode())
                print(client_socket.recv(1024).decode())
            case '2':
                client_socket.send('+EXIT\r\n'.encode())
            case _:
                break
