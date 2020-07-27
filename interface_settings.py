from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from interface_settings_slots import InterfaceSettingsPageSlots
from model import ProcessingObject

class InterfaceSettings(InterfaceSettingsPageSlots):
    
    def __init__(self, form, processingObject):
        super(InterfaceSettings, self).__init__()
        self.form = form
        self.setupUi(form, processingObject)
        self.connectSlots()