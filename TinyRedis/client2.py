import socket

HOST = '127.0.0.1'
PORT = 6379

with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        print('1. Send PING\n2. Send ECHO\n3. Send malformed command\n4. Send EXIT\n5. Exit client')
        match input():
            case '1':
                client_socket.send(b'*1\r\n$4\r\nPING\r\n')
                print(client_socket.recv(1024).decode())
            case '2':
                client_socket.send(b"*2\r\n$4\r\nECHO\r\n$32\r\nYou've probably heard me before!\r\n")
                print(client_socket.recv(1024).decode())
            case '3':
                client_socket.send(b'+PING\r\n')
                print(client_socket.recv(1024).decode())
            case '4':
                client_socket.send(b'*1\r\n$4\r\nEXIT\r\n')
            case _:
                break
