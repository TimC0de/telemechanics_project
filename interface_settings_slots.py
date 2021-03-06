from interface_settings_ui import Ui_Form
from PyQt5 import QtCore, QtWidgets
from devices_settings.mac_101_balance_page import Mac101BalanceSettingsPage
from devices_settings.mac_101_imbalance_page import Mac101ImbalanceSettingsPage
from devices_settings.mac_104_page import Mac104SettingsPage
from devices_settings.modbus_rtu import ModbusRtuSettingsPage

class InterfaceSettingsPageSlots(Ui_Form):

    def __init__(self):
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"
    
    def connectSlots(self):
        if self.asdu.interfaces[self.processingObject.processingInterfaceIndex].name != 'RS-485-1':
            self.setupButton.clicked.connect(self.openSettings)
        
        self.save.clicked.connect(self.saveSlot)
        self.cancel.clicked.connect(self.cancelSlot)

    def openSettings(self):
        if self.deviceNameSelector.currentIndex() > 0:
            window = QtWidgets.QWidget()
            window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
            if self.protocolSelector.currentText() == 'МЭК 101(Небалансный)':
                self.settings = Mac101ImbalanceSettingsPage(window, self.processingObject)
            elif self.protocolSelector.currentText() == "МЭК 101(Балансный)":
                self.settings = Mac101BalanceSettingsPage(window, self.processingObject)
            elif self.protocolSelector.currentText() == "MODBUS RTU":
                self.settings = ModbusRtuSettingsPage(window, self.processingObject)
            elif self.protocolSelector.currentText() == "МЭК 104":
                self.settings = Mac104SettingsPage(window, self.processingObject)
            window.show()