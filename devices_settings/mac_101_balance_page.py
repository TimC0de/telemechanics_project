from devices_settings import mac_101_balance_table, mac_101_balance_settings
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

class Mac101BalanceTablePage(mac_101_balance_table.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(Mac101BalanceTablePage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton.clicked.connect(self.openSettings)
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
        self.settings = Mac101BalanceSettingsPage(window, self.processingObject)
        window.show()
        self.form.hide()

class Mac101BalanceSettingsPage(mac_101_balance_settings.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(Mac101BalanceSettingsPage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton_2.clicked.connect(self.openTable)
        self.save.clicked.connect(self.saveSlot)
        self.cancel.clicked.connect(self.cancelSlot)

    def saveSlot(self):
        self.asdu.save(self.form)
        self.form.hide()

    def cancelSlot(self):
        self.asdu.cancel()
        self.form.hide()

    def openTable(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.table = Mac101BalanceTablePage(window, self.processingObject)
        window.show()
        self.form.hide()