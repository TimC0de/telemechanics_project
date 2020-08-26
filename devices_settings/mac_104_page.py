from devices_settings import mac_104_table, mac_104_settings, mac_104_timeouts
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget

class Mac104TablePage(mac_104_table.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(Mac104TablePage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton.clicked.connect(self.openSettings)
        self.pushButton_8.clicked.connect(self.openTimeouts)
        self.save.clicked.connect(self.saveSlot)
        self.cancel.clicked.connect(self.cancelSlot)

    def saveSlot(self):
        if self.processingObject.processTcpClient:
            self.td.forceSave()
        else:
            self.asdu.save(self.form)
        
        self.form.hide()

    def cancelSlot(self):
        if self.processingObject.processTcpClient:
            self.td.cancel()
        else:
            self.asdu.cancel()
        
        self.form.hide()

    def openSettings(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.settings = Mac104SettingsPage(window, self.processingObject)
        window.show()
        self.form.hide()

    def openTimeouts(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.timeouts = Mac104TimeoutsPage(window, self.processingObject)
        window.show()
        self.form.hide()

class Mac104SettingsPage(mac_104_settings.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(Mac104SettingsPage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton_2.clicked.connect(self.openTable)
        self.pushButton_4.clicked.connect(self.openTimeouts)
        self.save.clicked.connect(self.saveSlot)
        self.cancel.clicked.connect(self.cancelSlot)

    def saveSlot(self):
        if self.processingObject.processTcpClient:
            self.td.forceSave()
        else:
            self.asdu.save(self.form)
        
        self.form.hide()

    def cancelSlot(self):
        if self.processingObject.processTcpClient:
            self.td.cancel()
        else:
            self.asdu.cancel()

        self.form.hide()

    def openTable(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.table = Mac104TablePage(window, self.processingObject)
        window.show()
        self.form.hide()

    def openTimeouts(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.timeouts = Mac104TimeoutsPage(window, self.processingObject)
        window.show()
        self.form.hide()


class Mac104TimeoutsPage(mac_104_timeouts.Ui_Form):
    
    def __init__(self, form, processingObject):
        super(Mac104TimeoutsPage, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"

        self.connectSlots()

    def connectSlots(self):
        self.pushButton_2.clicked.connect(self.openTable)
        self.pushButton.clicked.connect(self.openSettings)
        self.save.clicked.connect(self.saveSlot)
        self.cancel.clicked.connect(self.cancelSlot)

    def saveSlot(self):
        if self.processingObject.processTcpClient:
            self.td.forceSave()
        else:
            self.asdu.save(self.form)
        
        self.form.hide()

    def cancelSlot(self):
        if self.processingObject.processTcpClient:
            self.td.cancel()
        else:
            self.asdu.cancel()
        
        self.form.hide()

    def openTable(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.table = Mac104TablePage(window, self.processingObject)
        window.show()
        self.form.hide()

    def openSettings(self):
        window = QWidget()
        window.setGeometry(self.form.rect().x(), self.form.rect().y(), self.form.rect().width(), self.form.rect().height())
        self.settings = Mac104SettingsPage(window, self.processingObject)
        window.show()
        self.form.hide()