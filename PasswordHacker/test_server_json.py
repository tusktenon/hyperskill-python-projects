# Test server for Stage 4
import json
import socket

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
                response = (
                    'Exception happened during login'
                    if PASSWORD.startswith(request_password)
                    else 'Wrong password!'
                )
            else:
                response = 'Connection success!'
            json_response = '{"result": "' + response + '"}'
            conn.send(json_response.encode())
