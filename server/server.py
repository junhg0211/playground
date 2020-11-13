from socket import socket
from threading import Thread


class ServerClient(Thread):
    def __init__(self, conn: socket, addr: tuple, server):
        super().__init__()
        self.conn = conn
        self.addr = addr
        self.server: Server = server
        self.setDaemon(True)

    def recv_raw(self, buffer_size: int) -> bytes:
        return self.conn.recv(buffer_size)

    def recv(self, buffer_size: int) -> str:
        return self.conn.recv(buffer_size).decode()

    def send_raw(self, data: bytes) -> int:
        self.conn.send(data)
        return len(data)

    def send(self, data: str) -> int:
        self.conn.send(data.encode())
        return len(data)

    def run(self) -> None:
        while self.server.running:
            pass  # todo client handling


class Server:
    def __init__(self, port: int = 51015):
        self.port = port
        self.running = False
        self.s = socket()
        self.clients = set()

    def run(self):
        while self.running:
            conn, addr = self.s.accept()
            server_client = ServerClient(conn, addr, self)
            server_client.start()
            self.clients.add(server_client)

    def start(self):
        self.s.bind(('', self.port))
        self.s.listen()
        self.running = True
