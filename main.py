import sys
import yaml
import config_util

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from main_slots import MainPageSlots
from model.TelemechanicsData import TelemechanicsData

class MainWindow(MainPageSlots):
    
    def __init__(self, form, td):
        super(MainWindow, self).__init__()
        self.form = form
        self.setupUi(form, td)
        self.connectSlots()

if __name__ == "__main__":  
    td = config_util.readYAML()

    app = QApplication(sys.argv)
    window = QWidget()
    ui = MainWindow(window, td)
    window.show()
    sys.exit(app.exec_())