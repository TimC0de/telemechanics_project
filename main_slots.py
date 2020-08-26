import yaml

from main_ui import Ui_Form
from PyQt5 import QtCore, QtWidgets, QtGui
from interface_settings import InterfaceSettings
from devices_settings.mac_104_page import Mac104SettingsPage

class MainPageSlots(Ui_Form):

    def __init__(self):
        self.interfaceType = "Ethernet"
        self.interface = "Ethernet-1"
        self.activeButtonStylesheet = "QPushButton {\n    background-color: #c4c4c4;\n    border-radius: 7px;\n    border: 0px;\n}"
        self.inactiveButtonStylesheet = "QPushButton {\n    background-color: white;\n    border-radius: 7px;\n    border: 0px;\n} QPushButton:hover { background-color: #e5e5e5; }"
    
    def connectSlots(self):
        # Interface settings menu
        self._translate = QtCore.QCoreApplication.translate

        # Save settings
        # self.save.clicked.connect(self.saveSlot)
        # self.cancel.clicked.connect(self.cancelSlot)
        # self.openFile.clicked.connect(self.openConfigFile)

    def saveSlot(self):
        self.currentASDU.save(self.form, mainPage=True)

    def cancelSlot(self):
        self.currentASDU.cancel()
        self.setASDUData(self.currentASDU.name)

        for child in self.scrollAreaWidgetContents.children():
            child.deleteLater()
        self.renderEthernetSettings(0, self.currentASDU)

    def openConfigFile(self):
        name = QtWidgets.QFileDialog.getOpenFileName(self.form, 'Открыть файл конфигурации УСПД')
        if name[0] == '' or name[0] == None:
            return
        
        with open(name[0], 'r', encoding="utf-16") as file:
            _translate = QtCore.QCoreApplication.translate
            asdu = yaml.load(file)
            asdu.path = name[0]
            self.processingObject.asdu = asdu
            self.currentASDU = asdu

            if not hasattr(self, "openFileCounter"):
                self.openFileCounter = 0
            else:
                self.openFileCounter += 1

            text = _translate("Form", self.currentASDU.name + " (Открытый)")
            self.comboBox.addItem(text + (" %d" % (self.openFileCounter) if self.openFileCounter > 0 else ""))

            index = self.comboBox.findText(text + (" %d" % (self.openFileCounter) if self.openFileCounter > 0 else ""), QtCore.Qt.MatchFixedString)
            self.comboBox.setCurrentIndex(index)
            self.asduNamePaths[text + (" %d" % (self.openFileCounter) if self.openFileCounter > 0 else "")] = asdu.path

            for child in self.scrollAreaWidgetContents.children():
                child.deleteLater()
            self.ethernetRendering(asdu)
            self.renderEthernetSettings(0, asdu)
            self.setASDUData(asdu)
            self.interfacesBlockRendering(0, 6)