import itertools
import socket
import string
import sys


def brute_force(client):
    chars = string.ascii_lowercase + string.digits
    for length in range(1, 64):
        for candidate in (''.join(t) for t in itertools.product(chars, repeat=length)):
            client.sendall(candidate.encode())
            response = client.recv(1024).decode()
            if response == 'Connection success!':
                return candidate
            if response == 'Too many attempts':
                return '[Too many attempts]'


def main():
    hostname, port = sys.argv[1:]
    address = (hostname, int(port))
    with socket.socket() as client:
        client.connect(address)
        print(brute_force(client))


if __name__ == '__main__':
    main()

