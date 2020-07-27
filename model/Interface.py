import yaml

class Interface:
    def __init__(self, name, protocols):
        self.name = name
        self.protocols = protocols
        self.settings = dict()