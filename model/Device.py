import yaml

class Device:
    def __init__(self, name, used, qty):
        self.name = name
        self.used = used
        self.qty = qty
        self.settings = dict()