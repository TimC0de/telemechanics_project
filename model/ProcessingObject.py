class ProcessingObject:
    def __init__(self, td):
        self.td = td
        self.asdu = None
        self.processingAsduIndex = -1
        self.processingInterfaceIndex = -1
        self.processingProtocolIndex = -1
        self.processingDeviceIndex = -1
        self.processingTcpClientIndex = -1
        self.processTcpClient = False