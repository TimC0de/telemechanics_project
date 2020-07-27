import sys
import math
import yaml
from model.TelemechanicsData import TelemechanicsData
from model.Asdu import Asdu
from model.Interface import Interface
from model.Protocol import Protocol
from model.Device import Device
from model.Ethernet import EthernetBridge, Ethernet
from model.TcpClient import TcpClient

def ASDUEthernetsGenerate(bridgesQty, ethernetQty):
    ethernets = list()
    for i in range(bridgesQty):
        ethernets.append(EthernetBridge(i))
    for i in range(ethernetQty):
        ethernets.append(Ethernet(u"Ethernet-%d" % (bridgesQty * 2 + i + 1)))
    return ethernets

def ProtocolDevicesGenerate(protocol):
    devices = list()
    for deviceName in [u"ТС-12", u"ТС-32", u"Пользовательское устройство"]:
        devices.append(Device(deviceName, True, ""))
    
    for deviceIndex in range(4, 31):
        devices.append(Device(u"Устройство %d" % (deviceIndex), False, ""))
    return devices

def InterfaceProtocolsGenerate(interface):
    if interface == "Ethernet":
        protocolNames = list([u"МЭК-104", u"61850"])
    else:
        protocolNames = list([u"МЭК-101 Балансный", u"МЭК-101 Небалансный", u"MODBUS RTU"])

    protocols = list()
    for protocolName in protocolNames:
        protocols.append(Protocol(protocolName, ProtocolDevicesGenerate(protocolName)))
    return protocols


def ASDUInterfacesGenerate():
    interfacesQty = {"Ethernet": 6, "RS-485": 5, "RS-232": 6, "CAN": 4}
    interfaces = list()
    for interface in interfacesQty:
        for interfaceIndex in range(interfacesQty[interface]):
            interfaces.append(Interface(u"%s-%d" % (interface, interfaceIndex + 1), InterfaceProtocolsGenerate(interface)))
    return interfaces

if __name__ == '__main__':
    print("Имя УСПД: ")
    name = str(input())
    print("Кол-во: ")
    qty = int(input())
    print("Кол-во мостов: ")
    bridgesQty = int(input())
    print("Кол-во Ethernet-ов: ")
    ethernetQty = int(input())
    print("Кол-во RS-485: ")
    rs485Qty = int(input())
    print("Кол-во RS-232: ")
    rs232Qty = int(input())
    print("Кол-во CAN: ")
    canQty = int(input())

    with open("./config/telemechanics.yaml", "r", encoding="utf-16") as file:
        td = yaml.load(file)
        if td.asduNames == None:
            td.asduNames = list()
        
        asdu = Asdu(name, qty, bridgesQty, ethernetQty, rs485Qty, rs232Qty, canQty, ASDUInterfacesGenerate(), ASDUEthernetsGenerate(bridgesQty, ethernetQty))
        asdu.forceSave()
        td.asduNames.append(asdu.name)
        td.forceSave()