import yaml

class Ethernet:
    def __init__(self, name):
        self.name = name
        self.settings = dict()

class Reservation:
    def __init__(self, name):
        self.name = name
        self.settings = dict()

class EthernetBridge:
    def __init__(self, bridgeIndex):
        startIndex = bridgeIndex * 2 + 1
        self.name = "Ethernet-%d,%d(Bridge)" % (startIndex, startIndex + 1)
        self.ethernet1 = Ethernet("Ethernet-%d" % (startIndex))
        self.ethernet2 = Ethernet("Ethernet-%d" % (startIndex + 1))
        self.reservationSettings = Reservation("Резервирование")