import yaml
from PyQt5 import QtWidgets
from model.Asdu import Asdu

class TelemechanicsData:
    def __init__(self, _deviceTypes, asduNames, tcpClients):
        self._deviceTypes = _deviceTypes
        self.asduNames = asduNames
        self.tcpClients = tcpClients

    def forceSave(self):
        with open('./config/telemechanics.yaml', "w", encoding="utf-16") as file:
            yaml.dump(self, stream=file, allow_unicode=True)