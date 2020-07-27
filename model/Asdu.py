import yaml
from PyQt5 import QtWidgets

class Asdu(yaml.YAMLObject):
    def __init__(self, name, quantity, bridgesQuantity, ethernetQuantity, rs485Quantity, rs232Quantity, canQuantity, interfaces, ethernets):
        self.name = name
        self.quantity = quantity
        self.bridgesQuantity = bridgesQuantity
        self.ethernetQuantity = ethernetQuantity
        self.rs485Quantity = rs485Quantity
        self.rs232Quantity = rs232Quantity
        self.canQuantity = canQuantity
        self.interfaces = interfaces
        self.ethernets = ethernets
        self.path = './config/asdus/' + name + '.yaml'

    def save(self, form, mainPage=False):
        if mainPage:
            name = QtWidgets.QFileDialog.getSaveFileName(form, 'Открыть файл конфигурации')
            if name[0] == '' or name[0] == None:
                return
            self.path = name[0]
        
        self.forceSave()

    def cancel(self):
        with open(self.path, "r", encoding="utf-16") as file:
            asdu = yaml.load(stream=file)
            self.name = asdu.name
            self.quantity = asdu.quantity
            self.bridgesQuantity = asdu.bridgesQuantity
            self.ethernetQuantity = asdu.ethernetQuantity
            self.rs485Quantity = asdu.rs485Quantity
            self.rs232Quantity = asdu.rs232Quantity
            self.canQuantity = asdu.canQuantity
            self.interfaces = asdu.interfaces
            self.ethernets = asdu.ethernets

    def forceSave(self):
        with open(self.path, "w", encoding="utf-16") as file:
            yaml.dump(self, stream=file, allow_unicode=True)

    @classmethod
    def to_yaml(cls, dumper, data):
        cleaned_data = dict((k, v) for (k, v) in data.__dict__.items() if k != 'path')
        return dumper.represent_mapping(cls.yaml_tag, cleaned_data)