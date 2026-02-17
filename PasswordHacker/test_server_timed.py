# Test server for Stage 5
import json
import socket
from time import sleep

HOST = '127.0.0.1'
PORT = 9090
LOGIN = 'admin'
PASSWORD = 'password'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            request = json.loads(data.decode())
            if not ('login' in request and 'password' in request):
                response = 'Bad request!'
            elif request['login'] != LOGIN:
                response = 'Wrong login!'
            elif (request_password := request['password']) != PASSWORD:
                if PASSWORD.startswith(request_password):
                    sleep(0.01)
                response = 'Wrong password!'
            else:
                response = 'Connection success!'
            json_response = '{"result": "' + response + '"}'
            conn.send(json_response.encode())
