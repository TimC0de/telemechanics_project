from devices_settings import modbus_rtu_registers, modbus_rtu_settings, modbus_rtu_discrets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

class ModbusRtuRegistersPage(modbus_rtu_registers.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(ModbusRtuRegistersPage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton.clicked.connect(self.openSettings)
        self.pushButton_8.clicked.connect(self.openDiscrets)
        self.save.clicked.connect(self.saveSlot)
        self.cancel.clicked.connect(self.cancelSlot)

    def saveSlot(self):
        self.asdu.save(self.form)
        self.form.hide()

    def cancelSlot(self):
        self.asdu.cancel()
        self.form.hide()

    def openSettings(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.settings = ModbusRtuSettingsPage(window, self.processingObject)
        window.show()
        self.form.hide()

    def openDiscrets(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.discrets = ModbusRtuDiscretsPage(window, self.processingObject)
        window.show()
        self.form.hide()

class ModbusRtuSettingsPage(modbus_rtu_settings.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(ModbusRtuSettingsPage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton_2.clicked.connect(self.openRegisters)
        self.pushButton_4.clicked.connect(self.openDiscrets)
        self.save.clicked.connect(self.saveSlot)
        self.cancel.clicked.connect(self.cancelSlot)

    def saveSlot(self):
        self.asdu.save(self.form)
        self.form.hide()

    def cancelSlot(self):
        self.asdu.cancel()
        self.form.hide()

    def openRegisters(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.registers = ModbusRtuRegistersPage(window, self.processingObject)
        window.show()
        self.form.hide()

    def openDiscrets(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.discrets = ModbusRtuDiscretsPage(window, self.processingObject)
        window.show()
        self.form.hide()

class ModbusRtuDiscretsPage(modbus_rtu_discrets.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(ModbusRtuDiscretsPage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton_2.clicked.connect(self.openRegisters)
        self.pushButton.clicked.connect(self.openSettings)
        self.save.clicked.connect(self.saveSlot)
        self.cancel.clicked.connect(self.cancelSlot)

    def saveSlot(self):
        self.asdu.save(self.form)
        self.form.hide()

    def cancelSlot(self):
        self.asdu.cancel()
        self.form.hide()

    def openRegisters(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.registers = ModbusRtuRegistersPage(window, self.processingObject)
        window.show()
        self.form.hide()

    def openSettings(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.settings = ModbusRtuSettingsPage(window, self.processingObject)
        window.show()
        self.form.hide()