import socket
import time
from threading import Thread

HOST = '0.0.0.0'
PORT = 6379


class ExpiringDatastore:
    def __init__(self):
        self._data = {}

    def __len__(self):
        return len(self._data)

    def __getitem__(self, key):
        if (expiry := self._data[key][1]) and expiry < time.time():
            del self._data[key]
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


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self._data = ExpiringDatastore()
        self._channels = {}
        self._exit_requested = False

    def run(self):
        with socket.socket() as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Set a timeout on server_socket.accept() to periodically check
            # the value of self._exit_requested
            server_socket.settimeout(5)
            server_socket.bind((HOST, PORT))
            server_socket.listen()
            while not self._exit_requested:
                try:
                    conn, addr = server_socket.accept()
                    Thread(target=self._handle_client, args=(conn,)).start()
                except TimeoutError:
                    pass

    def _handle_client(self, conn):
        with conn:
            while data := conn.recv(1024):
                try:
                    array = self.parse(data)
                    match (array[0], len(array)):
                        case ('GET', 2):
                            try:
                                conn.send(self.encode(self._data[array[1]]))
                            except KeyError:
                                conn.send(b'$-1\r\n')
                        case ('SET', 3):
                            self._data[array[1]] = (array[2], None)
                            conn.send(b'+OK\r\n')
                        case ('SET', 5) if array[3] == 'EX':
                            expiry = int(array[4])
                            if expiry < 0:
                                raise ValueError
                            self._data[array[1]] = (array[2], expiry)
                            conn.send(b'+OK\r\n')
                        case ('DEL', 2):
                            try:
                                del self._data[array[1]]
                            except KeyError:
                                pass
                            conn.send(b'+OK\r\n')
                        case ('PUBLISH', 3):
                            for subscriber in self._channels.get(array[1], set()):
                                subscriber.send(self.encode('message', array[2]))
                        case ('SUBSCRIBE', 2):
                            self._channels[array[1]] = self._channels.get(array[1], set()) | set((conn,))
                            conn.send(b'+OK\r\n')
                        case ('PING', 1):
                            conn.send(self.encode('PONG'))
                        case ('ECHO', 2):
                            conn.send(self.encode(array[1]))
                        case ('EXIT', 1):
                            self._exit_requested = True
                            return
                        case _:
                            conn.send(b'-Parsing error!\r\n')
                except ValueError:
                    conn.send(b'-Parsing error!\r\n')

    @staticmethod
    def encode(*strings):
        array = []
        for s in strings:
            array.append('$' + str(len(s)))
            array.append(s)
        return ('\r\n'.join(array) + '\r\n').encode()

    @staticmethod
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
    Server(HOST, PORT).run()


if __name__ == '__main__':
    main()
