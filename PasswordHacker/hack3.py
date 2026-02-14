from itertools import product
from socket import socket
from sys import argv


def dictionary_generator(password_list):
    for password in password_list:
        variations = ((x, y) if x != y else (x,) for (x, y) in zip(password, password.upper()))
        for variant in product(*variations):
            yield ''.join(variant)


def dictionary_hack(address, password_list):
    with socket() as client:
        client.connect(address)
        for candidate in dictionary_generator(password_list):
            client.sendall(candidate.encode())
            response = client.recv(1024).decode()
            if response == 'Connection success!':
                return candidate
        return None


def main():
    with open('passwords.txt') as file:
        password_list = file.read().splitlines()
    hostname, port = argv[1:]
    address = (hostname, int(port))
    print(dictionary_hack(address, password_list))


if __name__ == '__main__':
    main()

