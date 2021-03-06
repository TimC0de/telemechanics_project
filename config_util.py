import random
import yaml

from model.TelemechanicsData import TelemechanicsData
from model.Asdu import Asdu
from model.TcpClient import TcpClient
from model.Interface import Interface
from model.Protocol import Protocol
from model.Device import Device
from model.Ethernet import Ethernet, EthernetBridge

def ASDUEthernetsGenerate(bridgesQty, ethernetQty):
    ethernets = list()
    for i in range(bridgesQty):
        ethernets.append(EthernetBridge(i))
    for i in range(ethernetQty):
        ethernets.append(Ethernet(u"Ethernet-%d" % (bridgesQty * 2 + i + 1)))
    return ethernets

def ASDUTcpClientsGenerate():
    tcpClients = list()
    for tcpClientIndex in range(4):
        name = u"TCP клиент %d" % (tcpClientIndex + 1)
        tcpClients.append(TcpClient(name, True, "", "", "", u"МЭК-104", {'column_1': 'Параметры', 'column_2': 'Адрес', 'column_3': 'Период, c', 'column_4': 'Спорадическая', 'column_5': 'Апертура', 'column_6': 'Фоновое сканирование', 'column_7': 'Команды опроса'}, {'rowsCount': 12, 'columnCount': 7}))
    return tcpClients

def ProtocolDevicesGenerate(protocol):
    devices = list()
    for deviceIndex in range(1, 31):
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

def ASDUGenerate(asduIndex):
    bridgesQty = 0
    ethernetQty = 2
    canQty = 0
    rs232Qty = 0
    rs485Qty = 3
    asdu = Asdu(u"УСПД (Тест)", random.randrange(6), bridgesQty, ethernetQty, rs485Qty, rs232Qty, canQty, ASDUInterfacesGenerate(), ASDUEthernetsGenerate(bridgesQty, ethernetQty))
    with open(asdu.path, "w", encoding="utf-16") as file:
        yaml.dump(asdu, stream=file, allow_unicode=True)
    
    return asdu.name

def TelemechanicsGenerate(asdusQty = 1):
    asduNames = list()
    for i in range(asdusQty):
        asduNames.append(ASDUGenerate(i))
    return TelemechanicsData([u"ТС-12", u"ТС-32", u"Пользовательское устройство"], asduNames, ASDUTcpClientsGenerate())

def createYAML():
    with open("./config/telemechanics.yaml", "w", encoding="utf-16") as file:
        td = TelemechanicsGenerate()
        yaml.dump(td, stream=file, allow_unicode=True)
    return td

def readYAML():
    with open("./config/telemechanics.yaml", "r", encoding="utf-16") as file:
        td = yaml.load(stream=file)
    return td