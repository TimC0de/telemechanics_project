# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\interface_settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

import os
import yaml
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class Ui_Form(object):

    def setupUi(self, Form, processingObject):
        self.processingObject = processingObject
        self.asdu = processingObject.asdu
        self.title = self.asdu.interfaces[self.processingObject.processingInterfaceIndex].name

        Form.setObjectName("Form")
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        Form.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        Form.closeEvent = lambda event: self.closeEvent(event, self.asdu)
        self.form = Form
        self.setPageElements(Form)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(56, 199, 1076, 2))
        self.line.setStyleSheet("Line {\n"
"    border-color: #c4c4c4;\n"
"    color: #c4c4c4;\n"
"    background-color: #c4c4c4;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.scrollArea_2 = QtWidgets.QScrollArea(Form)
        self.scrollArea_2.setGeometry(QtCore.QRect(56, 231, 310, 380))
        self.scrollArea_2.setMinimumSize(QtCore.QSize(310, 380))
        self.scrollArea_2.setStyleSheet("QScrollArea { border: none; }")
        self.scrollArea_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")        
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(405, 240, 729, 380))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(410, 650, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton { border-radius: 5px; background-color: #FED2AA; }")
        self.save.setObjectName("save")
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(655, 650, 200, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("QPushButton { border-radius: 5px; background-color: #C4C4C4; }")
        self.cancel.setObjectName("cancel")
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setProtocolDevices(0)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def closeEvent(self, event, obj):
        obj.cancel()

    def setPageElements(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(56, 44, 900, 116 if 'Ethernet' in self.asdu.interfaces[self.processingObject.processingInterfaceIndex].name else 140))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 200, 70))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.protocolSelector = QtWidgets.QComboBox(self.frame_2)
        self.protocolSelector.setGeometry(QtCore.QRect(0, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.protocolSelector.setFont(font)
        self.protocolSelector.setStyleSheet("QComboBox { background-color: rgba(196, 196, 196, 30); border: none; }")
        self.protocolSelector.setEditable(False)
        self.protocolSelector.setObjectName("protocolSelector")

        if 'Ethernet' in self.asdu.interfaces[self.processingObject.processingInterfaceIndex].name:
                self.label = QtWidgets.QLabel(self.frame_2)
                self.label.setGeometry(QtCore.QRect(0, 0, 200, 40))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.frame_3 = QtWidgets.QFrame(self.frame)
                self.frame_3.setGeometry(QtCore.QRect(250, 0, 200, 70))
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.keepAlive = QtWidgets.QLineEdit(self.frame_3)
                self.keepAlive.setGeometry(QtCore.QRect(0, 40, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.keepAlive.setFont(font)
                self.keepAlive.setObjectName("keepAlive")
                self.keepAlive.setValidator(QIntValidator(self.frame_3))
                self.label_2 = QtWidgets.QLabel(self.frame_3)
                self.label_2.setGeometry(QtCore.QRect(0, 0, 200, 40))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.frame_4 = QtWidgets.QFrame(self.frame)
                self.frame_4.setGeometry(QtCore.QRect(500, 0, 200, 70))
                self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                self.asduAddress = QtWidgets.QLineEdit(self.frame_4)
                self.asduAddress.setGeometry(QtCore.QRect(0, 40, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.asduAddress.setFont(font)
                self.asduAddress.setObjectName("asduAddress")
                self.asduAddress.setValidator(QIntValidator(self.frame_4))
                self.label_3 = QtWidgets.QLabel(self.frame_4)
                self.label_3.setGeometry(QtCore.QRect(0, 0, 200, 40))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.frame_24 = QtWidgets.QFrame(self.frame)
                self.frame_24.setGeometry(QtCore.QRect(0, 76, 451, 40))
                self.frame_24.setStyleSheet("QFrame { border: none; }")
                self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_24.setObjectName("frame_24")
                self.boostTCP = QtWidgets.QCheckBox(self.frame_24)
                self.boostTCP.setGeometry(QtCore.QRect(0, 0, 451, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.boostTCP.setFont(font)
                self.boostTCP.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
                self.boostTCP.setObjectName("boostTCP")

                self.setupButton = QtWidgets.QPushButton(self.frame)
                self.setupButton.setGeometry(QtCore.QRect(500, 80, 200, 35))
                font = QtGui.QFont()
                font.setPointSize(10)
                self.setupButton.setFont(font)
                self.setupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                self.setupButton.setStyleSheet("QPushButton { background-color: #FED2AA; border: none; border-radius: 5px; }")
                self.setupButton.setObjectName("setupButton")
                self.setupButton.setText(_translate("Form", "Настроить"))
        else:
                self.label = QtWidgets.QLabel(self.frame_2)
                self.label.setGeometry(QtCore.QRect(0, 0, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.frame_3 = QtWidgets.QFrame(self.frame)
                self.frame_3.setGeometry(QtCore.QRect(250, 0, 200, 60))
                self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_3.setObjectName("frame_3")
                self.parity = QtWidgets.QComboBox(self.frame_3)
                self.parity.setGeometry(QtCore.QRect(0, 30, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.parity.setFont(font)
                self.parity.setObjectName("parity")
                self.parity.addItems(["Четный", "Нечетный", "Нет"])
                self.parity.setStyleSheet("QComboBox { background-color: rgba(196, 196, 196, 30); border: none; }")
                self.label_2 = QtWidgets.QLabel(self.frame_3)
                self.label_2.setGeometry(QtCore.QRect(0, 0, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.label_2.setFont(font)
                self.label_2.setObjectName("label_2")
                self.frame_4 = QtWidgets.QFrame(self.frame)
                self.frame_4.setGeometry(QtCore.QRect(500, 0, 200, 60))
                self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_4.setObjectName("frame_4")
                self.asduAddress = QtWidgets.QLineEdit(self.frame_4)
                self.asduAddress.setGeometry(QtCore.QRect(0, 30, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.asduAddress.setFont(font)
                self.asduAddress.setObjectName("asduAddress")
                self.asduAddress.setValidator(QIntValidator(self.frame_4))
                self.label_3 = QtWidgets.QLabel(self.frame_4)
                self.label_3.setGeometry(QtCore.QRect(0, 0, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.label_3.setFont(font)
                self.label_3.setObjectName("label_3")
                self.frame_5 = QtWidgets.QFrame(self.frame)
                self.frame_5.setGeometry(QtCore.QRect(0, 80, 200, 60))
                self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_5.setObjectName("frame_5")
                self.speed = QtWidgets.QComboBox(self.frame_5)
                self.speed.setGeometry(QtCore.QRect(0, 30, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.speed.setFont(font)
                self.speed.setObjectName("speed")
                self.speed.addItems(["75", "110", "134", "150", "300", "600", "1200", "1800", "2400", "4800", "7200", "9600", "14400", "19200", "38400", "57600", "115200", "128000"])
                self.speed.setStyleSheet("QComboBox { background-color: rgba(196, 196, 196, 30); border: none; }")
                self.label_4 = QtWidgets.QLabel(self.frame_5)
                self.label_4.setGeometry(QtCore.QRect(0, 0, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.label_4.setFont(font)
                self.label_4.setObjectName("label_4")
                self.frame_6 = QtWidgets.QFrame(self.frame)
                self.frame_6.setGeometry(QtCore.QRect(250, 80, 200, 60))
                self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
                self.frame_6.setObjectName("frame_6")
                self.stopBits = QtWidgets.QComboBox(self.frame_6)
                self.stopBits.setGeometry(QtCore.QRect(0, 30, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(9)
                self.stopBits.setFont(font)
                self.stopBits.setObjectName("stopBits")
                self.stopBits.addItems(["1", "1.5", "2"])
                self.stopBits.setStyleSheet("QComboBox { background-color: rgba(196, 196, 196, 30); border: none; }")
                self.label_5 = QtWidgets.QLabel(self.frame_6)
                self.label_5.setGeometry(QtCore.QRect(0, 0, 200, 30))
                font = QtGui.QFont()
                font.setPointSize(11)
                self.label_5.setFont(font)
                self.label_5.setObjectName("label_5")

                if self.asdu.interfaces[self.processingObject.processingInterfaceIndex].name == 'RS-485-1':
                    self.rs4851Label = QtWidgets.QLabel(self.frame)
                    self.rs4851Label.setGeometry(QtCore.QRect(500, 105, 400, 35))
                    font = QtGui.QFont()
                    font.setPointSize(11)
                    self.rs4851Label.setFont(font)
                    self.rs4851Label.setStyleSheet("QLabel { border: none; }")
                    self.rs4851Label.setObjectName("rs4851Label")
                    self.rs4851Label.setText(_translate("Form", "RS-485-1 зарезервирован АСКУЭ"))
                else:
                    self.setupButton = QtWidgets.QPushButton(self.frame)
                    self.setupButton.setGeometry(QtCore.QRect(500, 105, 200, 35))
                    font = QtGui.QFont()
                    font.setPointSize(10)
                    self.setupButton.setFont(font)
                    self.setupButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    self.setupButton.setStyleSheet("QPushButton { background-color: #FED2AA; border: none; border-radius: 5px; }")
                    self.setupButton.setObjectName("setupButton")
                    self.setupButton.setText(_translate("Form", "Настроить"))
                
        self.setInterfaceProperties()
        protocolSelectorItems = ["МЭК 104", "61850"] if 'Ethernet' in self.asdu.interfaces[self.processingObject.processingInterfaceIndex].name else ['МЭК 101(Балансный)', 'МЭК 101(Небалансный)', 'MODBUS RTU']
        self.protocolSelector.addItems([_translate("Form", protocolSelectorItem) for protocolSelectorItem in protocolSelectorItems])
        self.protocolSelector.currentIndexChanged.connect(self.protocolChanged)

    def setInterfaceProperties(self):
        _translate = QtCore.QCoreApplication.translate
        if "Ethernet" in self.asdu.interfaces[self.processingObject.processingInterfaceIndex].name:
            self.keepAlive.setText(self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings.get("keepAlive"))
            self.keepAlive.editingFinished.connect(self.interfaceEditionCallback("keepAlive"))
            self.label_2.setText(_translate("Form", "TCP Keep Alive:"))
            self.asduAddress.setText(self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings.get("asduAddress"))
            self.asduAddress.editingFinished.connect(self.interfaceEditionCallback("asduAddress"))
            self.label_3.setText(_translate("Form", "ASDU адрес УСПД:"))
            self.boostTCP.setText(_translate("Form", "Ускорить TCP повторной отправкой?"))
            self.boostTCP.setChecked(self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings.get("boostTCP") or False)
            self.boostTCP.stateChanged.connect(self.interfaceCheckCallback("boostTCP"))
        else:
            self.parity.setCurrentText(self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings.get("parity") or 'Четный')
            self.parity.currentIndexChanged.connect(self.interfaceSelectionCallback("parity"))
            self.label_2.setText(_translate("Form", "Четность:"))
            self.asduAddress.setText(self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings.get("asduAddress"))
            self.asduAddress.editingFinished.connect(self.interfaceEditionCallback("asduAddress"))
            self.label_3.setText(_translate("Form", "ASDU адрес УСПД:"))

            self.speed.setCurrentText(self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings.get("speed") or '19200')
            self.speed.currentIndexChanged.connect(self.interfaceSelectionCallback("speed"))
            self.label_4.setText(_translate("Form", "Скорость:"))

            self.stopBits.setCurrentText(self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings.get("stopBits") or '1')
            self.stopBits.currentIndexChanged.connect(self.interfaceSelectionCallback("stopBits"))
            self.label_5.setText(_translate("Form", "Стоповые биты:"))

    def interfaceEditionCallback(self, field):
        return lambda: self.updateInterfaceText(field)

    def interfaceSelectionCallback(self, field):
        return lambda: self.updateInterfaceCurrentItem(field)

    def updateInterfaceText(self, field):
        self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings[field] = getattr(self, field).text()

    def updateInterfaceCurrentItem(self, field):
        self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings[field] = getattr(self, field).currentText()

    def interfaceCheckCallback(self, field):
        return lambda: self.updateInterfaceState(field)

    def updateInterfaceState(self, field):
        self.asdu.interfaces[self.processingObject.processingInterfaceIndex].settings[field] = getattr(self, field).isChecked()

    def protocolChanged(self):
        for child in self.scrollAreaWidgetContents_2.children():
                child.deleteLater()

        self.setProtocolDevices(self.protocolSelector.currentIndex())

    def deviceSettingsUI(self, device):
        _translate = QtCore.QCoreApplication.translate
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 727, 555))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget_13 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_13.setGeometry(QtCore.QRect(0, 0, 727, 378))
        self.widget_13.setStyleSheet("QFrame {\n"
"    border: 1.5px solid #999999;\n"
"}")
        self.widget_13.setObjectName("widget_13")
        self.quantityFrame = QtWidgets.QFrame(self.widget_13)
        self.quantityFrame.setGeometry(QtCore.QRect(35, 183, 200, 70))
        self.quantityFrame.setStyleSheet("QFrame { border: none; }")
        self.quantityFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.quantityFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.quantityFrame.setObjectName("quantityFrame")
        self.quantityLabel = QtWidgets.QLabel(self.quantityFrame)
        self.quantityLabel.setGeometry(QtCore.QRect(0, 0, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.quantityLabel.setFont(font)
        self.quantityLabel.setObjectName("quantityLabel")
        self.quantityInput = QtWidgets.QLineEdit(self.quantityFrame)
        self.quantityInput.setGeometry(QtCore.QRect(0, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.quantityInput.setFont(font)
        self.quantityInput.setStyleSheet("QLineEdit { border: 1px solid #aaaaaa; }")
        self.quantityInput.setObjectName("quantityInput")
        self.quantityInput.setValidator(QIntValidator(0, 30, self.quantityFrame))
        self.usedCheckboxFrame = QtWidgets.QFrame(self.widget_13)
        self.usedCheckboxFrame.setGeometry(QtCore.QRect(35, 122, 155, 40))
        self.usedCheckboxFrame.setStyleSheet("QFrame { border: none; }")
        self.usedCheckboxFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.usedCheckboxFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.usedCheckboxFrame.setObjectName("usedCheckboxFrame")
        self.usedCheckbox = QtWidgets.QCheckBox(self.usedCheckboxFrame)
        self.usedCheckbox.setGeometry(QtCore.QRect(0, 0, 155, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.usedCheckbox.setFont(font)
        self.usedCheckbox.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.usedCheckbox.setObjectName("usedCheckbox")
        
        self.deviceNameFrame = QtWidgets.QFrame(self.widget_13)
        self.deviceNameFrame.setGeometry(QtCore.QRect(35, 21, 200, 70))
        self.deviceNameFrame.setStyleSheet("QFrame { border: none; }")
        self.deviceNameFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.deviceNameFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.deviceNameFrame.setObjectName("deviceNameFrame")
        self.deviceNameSelector = QtWidgets.QComboBox(self.deviceNameFrame)
        self.deviceNameSelector.setGeometry(QtCore.QRect(0, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.deviceNameSelector.setFont(font)
        self.deviceNameSelector.setStyleSheet("QComboBox {\n"
"    background-color: rgba(196, 196, 196, 30);\n"
"    border: none;\n"
"}\n"
"")
        self.deviceNameSelector.setEditable(False)
        self.deviceNameSelector.setObjectName("deviceNameSelector")
        self.deviceNameSelector.addItems(["Выберите тип устройства"] + [file[:file.find('.yaml')] for file in os.listdir("./config/devices/%s" % self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.currentProtocolIndex].name)])
        self.deviceNameLabel = QtWidgets.QLabel(self.deviceNameFrame)
        self.deviceNameLabel.setGeometry(QtCore.QRect(0, 0, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.deviceNameLabel.setFont(font)
        self.deviceNameLabel.setObjectName("deviceNameLabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.label.setText(_translate("Form", "Выберите протокол:"))
        self.quantityLabel.setText(_translate("Form", "Колличество:"))
        self.usedCheckbox.setText(_translate("Form", "Используется"))
        self.deviceNameLabel.setText(_translate("Form", "Имя устройства:"))

        index = self.deviceNameSelector.findText(device.name, QtCore.Qt.MatchFixedString)
        self.deviceNameSelector.setCurrentIndex(index if index >= 0 else 0)
        self.deviceNameSelector.currentIndexChanged.connect(self.updateDeviceText)

        self.quantityInput.setText(device.qty)
        self.quantityInput.editingFinished.connect(self.updateDeviceQuantity)

        self.usedCheckbox.setChecked(device.used)
        self.usedCheckbox.stateChanged.connect(self.updateDeviceUsedProperty)

    def saveSlot(self):
        self.asdu.save(self.form)
        self.form.hide()

    def cancelSlot(self):
        self.asdu.cancel()
        self.form.hide()

    def updateDeviceText(self):
        device = self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.currentProtocolIndex].devices[self.currentDeviceIndex]
        
        if self.deviceNameSelector.currentIndex() > 0:
            with open("./config/devices/%s/%s.yaml" % (self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.currentProtocolIndex].name, self.deviceNameSelector.currentText()), "r", encoding="utf-16") as file:
                connectableDevice = yaml.load(stream=file)
                device.columnNames = connectableDevice.columnNames
                device.settings = connectableDevice.settings
                device.data = connectableDevice.data
                getattr(self, "device_%d" % (self.currentDeviceIndex)).setText(self.deviceNameSelector.currentText())
                device.name = self.deviceNameSelector.currentText()
        else:
            getattr(self, "device_%d" % (self.currentDeviceIndex)).setText("Устройство %d" % (self.currentDeviceIndex + 1))
            device.name = "Устройство %d" % (self.currentDeviceIndex + 1)

    def updateDeviceQuantity(self):
        deviceQuantity = self.quantityInput.text()
        if deviceQuantity != '':
            currentDevice = self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.currentProtocolIndex].devices[self.currentDeviceIndex]
            currentDevice.qty = deviceQuantity
            for deviceIndex in range(self.currentDeviceIndex + 1, self.currentDeviceIndex + int(deviceQuantity.replace("\xa0", ""))):
                    device = self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.currentProtocolIndex].devices[deviceIndex]
                    device.name = currentDevice.name
                    device.columnNames = currentDevice.columnNames
                    device.settings = currentDevice.settings
                    device.data = currentDevice.data
                    device.used = True
                    getattr(self, "device_%d" % (deviceIndex)).setText(currentDevice.name)
                    getattr(self, "device_%d" % (deviceIndex)).setStyleSheet("QPushButton { background-color: white; border: 0px; border-radius: 7px; color: black; }")

    def updateDeviceUsedProperty(self):
        self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.currentProtocolIndex].devices[self.currentDeviceIndex].used = self.usedCheckbox.isChecked()

    def setProtocolDevices(self, protocolIndex):
        self.processingObject.processingProtocolIndex = protocolIndex
        self.currentProtocolIndex = protocolIndex

        protocol = self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[protocolIndex]
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 293, 998))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox.setMinimumSize(QtCore.QSize(272, 30 * 49))
        self.groupBox.setStyleSheet("QGroupBox { border: none; }")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")

        _translate = QtCore.QCoreApplication.translate
        font = QtGui.QFont()
        font.setPointSize(11)
        deviceIndex = 0
        for device in protocol.devices:
                button = QtWidgets.QPushButton(self.groupBox)
                button.setGeometry(QtCore.QRect(0, deviceIndex * 49, 271, 49))
                button.setFont(font)
                button.setStyleSheet("QPushButton { background-color: %s; border: 0px; border-radius: 7px; color: %s; } %s" % ("#c4c4c4" if deviceIndex == 0 else "white", "black" if device.used or deviceIndex == 0 else "#c4c4c4", "" if deviceIndex == 0 else "QPushButton:hover { background-color: #e5e5e5; }"))
                button.setObjectName("device_%s" % (deviceIndex))
                button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                button.setText(_translate("Form", device.name))
                button.clicked.connect(self.clickedEvent(deviceIndex))
                setattr(self, "device_%s" % (deviceIndex), button)
                deviceIndex += 1

        self.verticalLayout.addWidget(self.groupBox)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.activateDevice(0)
        
    def clickedEvent(self, deviceIndex):
        return lambda: self.activateDevice(deviceIndex)

    def activateDevice(self, deviceIndex):
        self.currentDeviceIndex = deviceIndex
        self.processingObject.processingDeviceIndex = deviceIndex

        i = 0
        for device in self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.currentProtocolIndex].devices:
                getattr(self, "device_%s" % (i)).setStyleSheet("QPushButton { background-color: %s; border: 0px; border-radius: 7px; color: %s; } %s" % ("#c4c4c4" if i == deviceIndex else "white", "black" if device.used or i == deviceIndex else "#c4c4c4", "" if i == deviceIndex else "QPushButton:hover { background-color: #e5e5e5; }"))
                i += 1

        if hasattr(self, 'scrollAreaWidgetContents'):
                for child in self.scrollAreaWidgetContents.children():
                    child.deleteLater()

        self.deviceSettingsUI(self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.currentProtocolIndex].devices[deviceIndex])

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.title))
        self.save.setText(_translate("Form", "Сохранить"))
        self.cancel.setText(_translate("Form", "Отмена"))