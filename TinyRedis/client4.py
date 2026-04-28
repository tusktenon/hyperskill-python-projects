import socket

HOST = '0.0.0.0'
PORT = 6379

def encode(*strings):
    array = ['*' + str(len(strings))]
    for s in strings:
        array.append('$' + str(len(s)))
        array.append(s)
    return ('\r\n'.join(array) + '\r\n').encode()

with socket.socket() as client_socket:
    client_socket.connect((HOST, PORT))
    while True:
        cmd = input().split()
        if cmd[0] == 'quit':
            break
        else:
            encoded = encode(*cmd)
            print('Sending:', encoded)
            client_socket.send(encode(*cmd))
            print(client_socket.recv(1024).decode())
