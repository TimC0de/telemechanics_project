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
        self.save.clicked.connect(lambda: self.asdu.save(self.form))
        self.cancel.clicked.connect(self.cancelSlot)

    def cancelSlot(self):
        self.asdu.cancel()
        self.device = self.getDevice()

        for child in self.scrollAreaWidgetContents.children():
            child.deleteLater()
        self.settingsRender()

    def openSettings(self):
        window = QWidget()
        self.settings = Mac104SettingsPage(window, self.processingObject)
        window.show()
        self.form.hide()

    def openTimeouts(self):
        window = QWidget()
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
        self.save.clicked.connect(lambda: self.asdu.save(self.form))
        self.cancel.clicked.connect(self.cancelSlot)

    def cancelSlot(self):
        self.asdu.cancel()
        self.device = self.getDevice()

        for child in self.scrollAreaWidgetContents.children():
            child.deleteLater()
        self.settingsRender()

    def openTable(self):
        window = QWidget()
        self.table = Mac104TablePage(window, self.processingObject)
        window.show()
        self.form.hide()

    def openTimeouts(self):
        window = QWidget()
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
        self.save.clicked.connect(lambda: self.asdu.save(self.form))
        self.cancel.clicked.connect(self.cancelSlot)

    def cancelSlot(self):
        self.asdu.cancel()
        self.device = self.getDevice()

        for child in self.scrollAreaWidgetContents.children():
            child.deleteLater()
        self.timeoutsRender()

    def openTable(self):
        window = QWidget()
        self.table = Mac104TablePage(window, self.processingObject)
        window.show()
        self.form.hide()

    def openSettings(self):
        window = QWidget()
        self.settings = Mac104SettingsPage(window, self.processingObject)
        window.show()
        self.form.hide()