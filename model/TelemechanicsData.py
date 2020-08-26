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

    def cancel(self):
        with open('./config/telemechanics.yaml', "r", encoding="utf-16") as file:
            td = yaml.load(stream=file)
            self._deviceTypes = td._deviceTypes
            self.asduNames = td.asduNames
            self.tcpClients = td.tcpClients