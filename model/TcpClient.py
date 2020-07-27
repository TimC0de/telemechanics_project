import yaml

class TcpClient:
    def __init__(self, name, used, ip, port, keepAlive, protocol):
        self.name = name
        self.used = used
        self.ip = ip
        self.port = port
        self.keepAlive = keepAlive
        self.protocol = protocol
        self.settings = dict()