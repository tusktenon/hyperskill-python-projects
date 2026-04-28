import socket
import time

HOST = '0.0.0.0'
PORT = 6379


class ExpiringDatastore:
    def __init__(self):
        self._data = {}

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        return self._data[key][0]

    def __setitem__(self, key, value):
        expiry = time.time() + value[1] if value[1] else None
        self._data[key] = (value[0], expiry)

    def __delitem__(self, key):
        del self._data[key]

    def __contains__(self, obj):
        return obj in self._data

    def __iter__(self):
        yield from self._data

    def cleanup(self):
        # can't remove keys from a dictionary while iterating through it,
        # so iterate through a copy of the keys
        for key in [k for k in self._data if self._is_expired(k)]:
            del self[key]

    def _is_expired(self, key):
        return (expiry := self._data[key][1]) and expiry < time.time()


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
    datastore = ExpiringDatastore()
    with socket.socket() as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        while True:
            conn, addr = server_socket.accept()
            with conn:
                while data := conn.recv(1024):
                    # remove expired entries before processing next request
                    datastore.cleanup()
                    try:
                        array = parse(data)
                        match (array[0], len(array)):
                            case ('GET', 2):
                                try:
                                    conn.send(encode(datastore[array[1]]))
                                except KeyError:
                                    conn.send(b'$-1\r\n')
                            case ('SET', 3):
                                datastore[array[1]] = (array[2], None)
                                conn.send(b'+OK\r\n')
                            case ('SET', 5) if array[3] == 'EX':
                                expiry = int(array[4])
                                if expiry < 0:
                                    raise ValueError
                                datastore[array[1]] = (array[2], expiry)
                                conn.send(b'+OK\r\n')
                            case ('DEL', 2):
                                try:
                                    del datastore[array[1]]
                                except KeyError:
                                    pass
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
