import socket


class CommonClient:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.ipaddr = socket.gethostbyname(self.hostname)

