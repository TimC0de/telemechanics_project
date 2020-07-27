from devices_settings import mac_101_imbalance_table, mac_101_imbalance_settings
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

class Mac101ImbalanceTablePage(mac_101_imbalance_table.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(Mac101ImbalanceTablePage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton.clicked.connect(self.openSettings)
        self.save.clicked.connect(lambda: self.asdu.save(self.form))
        self.cancel.clicked.connect(self.cancelSlot)

    def cancelSlot(self):
        self.asdu.cancel()
        self.device = self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.processingObject.processingProtocolIndex].devices[self.processingObject.processingDeviceIndex]

        for child in self.scrollAreaWidgetContents.children():
            child.deleteLater()
        self.settingsRender()

    def openSettings(self):
        window = QWidget()
        self.settings = Mac101ImbalanceSettingsPage(window, self.processingObject)
        window.show()
        self.form.hide()

class Mac101ImbalanceSettingsPage(mac_101_imbalance_settings.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(Mac101ImbalanceSettingsPage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton_2.clicked.connect(self.openTable)
        self.save.clicked.connect(lambda: self.asdu.save(self.form))
        self.cancel.clicked.connect(self.cancelSlot)

    def cancelSlot(self):
        self.asdu.cancel()
        self.device = self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.processingObject.processingProtocolIndex].devices[self.processingObject.processingDeviceIndex]

        for child in self.scrollAreaWidgetContents.children():
            child.deleteLater()
        self.settingsRender()

    def openTable(self):
        window = QWidget()
        self.table = Mac101ImbalanceTablePage(window, self.processingObject)
        window.show()
        self.form.hide()
