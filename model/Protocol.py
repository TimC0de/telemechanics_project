import yaml
from model.Device import Device

class Protocol:
    def __init__(self, name, devices):
        self.name = name
        self.devices = devices