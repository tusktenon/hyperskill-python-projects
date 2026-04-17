import socket

HOST = '0.0.0.0'
PORT = 6379


def encode(*strings):
    array = []
    for s in strings:
        array.append('$' + str(len(s)))
        array.append(s)
    return ('\r\n'.join(array) + '\r\n').encode()


def parse(data):
    if not data.endswith(b'\r\n'):
        raise ValueError()

    items, *bulk_strings = data.removesuffix(b'\r\n').split(b'\r\n')

    if not (items.startswith(b'*') and 2 * int(items.removeprefix(b'*')) == len(bulk_strings)):
        raise ValueError()

    decoded = []
    while bulk_strings:
        length, string, *bulk_strings = bulk_strings
        if not (length.startswith(b'$') and int(length.removeprefix(b'$')) == len(string)):
            raise ValueError()
        decoded.append(string.decode())

    return decoded


def main():
    database = {}
    with socket.socket() as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        while True:
            conn, addr = server_socket.accept()
            with conn:
                while data := conn.recv(1024):
                    try:
                        array = parse(data)
                        match (array[0], len(array)):
                            case ('GET', 2):
                                try:
                                    conn.send(encode(database[array[1]]))
                                except KeyError:
                                    conn.send(b'$-1\r\n')
                            case ('SET', 3):
                                database[array[1]] = array[2]
                                conn.send(b'+OK\r\n')
                            case ('PING', 1):
                                conn.send(encode('PONG'))
                            case ('ECHO', 2):
                                conn.send(encode(array[1]))
                            case ('EXIT', 1):
                                exit(0)
                            case _:
                                conn.send(b'-Parsing error!\r\n')
                    except ValueError:
                        conn.send(b'-Parsing error!\r\n')


if __name__ == '__main__':
    main()
