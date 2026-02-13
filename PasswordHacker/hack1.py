import socket
import sys

args = sys.argv
hostname, port, data = args[1], int(args[2]), args[3]
with socket.socket() as client:
    client.connect((hostname, port))
    client.sendall(data.encode())
    response = client.recv(1024).decode()
    print(response)
