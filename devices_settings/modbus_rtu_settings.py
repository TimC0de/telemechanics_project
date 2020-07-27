# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\modbus_rtu_settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form, processingObject):
        self.processingObject = processingObject
        self.asdu = processingObject.asdu
        self.device = self.asdu.interfaces[processingObject.processingInterfaceIndex].protocols[processingObject.processingProtocolIndex].devices[processingObject.processingDeviceIndex]

        Form.setObjectName("Form")
        Form.resize(1366, 768)
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        Form.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        self.form = Form
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 40, 1366, 728))
        self.scrollArea.setMinimumSize(QtCore.QSize(310, 380))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.frame_8 = QtWidgets.QFrame(Form)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 1366, 40))
        self.frame_8.setStyleSheet("QFrame { background-color: #c4c4c4; }")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.pushButton = QtWidgets.QPushButton(self.frame_8)
        self.pushButton.setGeometry(QtCore.QRect(40, 10, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton { border: none; border-top-left-radius: 5px; border-top-right-radius: 5px; }")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 10, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton { border: none; border-top-left-radius: 5px; border-top-right-radius: 5px; background-color: transparent; }")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 10, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton { border: none; border-top-left-radius: 5px; border-top-right-radius: 5px; background-color: transparent; }")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingsRender()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def settingsRender(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1366, 728))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(1366, 728))
        self.groupBox.setStyleSheet("QGroupBox { border: none; }")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(40, 285, 1286, 2))
        self.line.setStyleSheet("Line {\n"
"    border: none;\n"
"    background-color: #c4c4c4;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame_9 = QtWidgets.QFrame(self.groupBox)
        self.frame_9.setGeometry(QtCore.QRect(40, 67, 531, 200))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.label_8 = QtWidgets.QLabel(self.frame_9)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 380, 60))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.frame_16 = QtWidgets.QFrame(self.frame_9)
        self.frame_16.setGeometry(QtCore.QRect(0, 130, 200, 70))
        self.frame_16.setStyleSheet("QFrame { border: none; }")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_15 = QtWidgets.QLabel(self.frame_16)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.interval = QtWidgets.QLineEdit(self.frame_16)
        self.interval.setGeometry(QtCore.QRect(0, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.interval.setFont(font)
        self.interval.setStyleSheet("QLineEdit { border: 1px solid #aaaaaa; }")
        self.interval.setObjectName("interval")
        self.frame_24 = QtWidgets.QFrame(self.frame_9)
        self.frame_24.setGeometry(QtCore.QRect(0, 80, 531, 40))
        self.frame_24.setStyleSheet("QFrame { border: none; }")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.cicleTransfer = QtWidgets.QCheckBox(self.frame_24)
        self.cicleTransfer.setGeometry(QtCore.QRect(0, 0, 531, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cicleTransfer.setFont(font)
        self.cicleTransfer.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.cicleTransfer.setObjectName("cicleTransfer")
        self.frame_10 = QtWidgets.QFrame(self.groupBox)
        self.frame_10.setGeometry(QtCore.QRect(40, 290, 531, 150))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.label_9 = QtWidgets.QLabel(self.frame_10)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 380, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.frame_25 = QtWidgets.QFrame(self.frame_10)
        self.frame_25.setGeometry(QtCore.QRect(0, 110, 531, 40))
        self.frame_25.setStyleSheet("QFrame { border: none; }")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.fixedData = QtWidgets.QCheckBox(self.frame_25)
        self.fixedData.setGeometry(QtCore.QRect(0, 0, 531, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fixedData.setFont(font)
        self.fixedData.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.fixedData.setObjectName("fixedData")
        self.frame_26 = QtWidgets.QFrame(self.frame_10)
        self.frame_26.setGeometry(QtCore.QRect(0, 60, 300, 40))
        self.frame_26.setStyleSheet("QFrame { border: none; }")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.fastChanges = QtWidgets.QCheckBox(self.frame_26)
        self.fastChanges.setGeometry(QtCore.QRect(0, 0, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.fastChanges.setFont(font)
        self.fastChanges.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.fastChanges.setObjectName("fastChanges")
        self.save = QtWidgets.QPushButton(self.groupBox)
        self.save.setGeometry(QtCore.QRect(1000, 67, 155, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton { border-radius: 5px; background-color: #FED2AA; }")
        self.save.setObjectName("save")
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel = QtWidgets.QPushButton(self.groupBox)
        self.cancel.setGeometry(QtCore.QRect(800, 67, 155, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("QPushButton { border-radius: 5px; background-color: #C4C4C4; }")
        self.cancel.setObjectName("cancel")
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verticalLayout.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        _translate = QtCore.QCoreApplication.translate
        self.label_8.setText(_translate("Form", "MODBUS RTU (%s)" % (self.device.name)))
        self.label_15.setText(_translate("Form", "Интервал, с:"))
        self.cicleTransfer.setText(_translate("Form", "Циклическая передача(Для индикации, макс. 125 регистров)"))
        self.label_9.setText(_translate("Form", "Тип данных"))
        self.fixedData.setText(_translate("Form", "Фиксированные данные(Без необходимости не включать)"))
        self.fastChanges.setText(_translate("Form", "Быстрые изменения"))
        self.save.setText(_translate("Form", "Сохранить"))
        self.cancel.setText(_translate("Form", "Отмена"))

        keyTypes = {"interval": "text",
         "cicleTransfer": "boolean",
            "fastChanges": "boolean",
             "fixedData": "boolean"}

        for key in keyTypes:
                if keyTypes[key] == "text":
                        getattr(self, key).setText(self.device.settings.get(key))
                        getattr(self, key).editingFinished.connect(self.editionCallback(key))
                else:
                        getattr(self, key).setChecked(self.device.settings.get(key) or False)
                        getattr(self, key).stateChanged.connect(self.checkCallback(key))

    def editionCallback(self, field):
        return lambda: self.updateDeviceText(field)

    def updateDeviceText(self, field):
        self.device.settings[field] = getattr(self, field).text()

    def checkCallback(self, field):
        return lambda: self.updateDeviceState(field)

    def updateDeviceState(self, field):
        self.device.settings[field] = getattr(self, field).isChecked()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.device.name))
        self.pushButton.setText(_translate("Form", "Настройки"))
        self.pushButton_2.setText(_translate("Form", "Регистры"))
        self.pushButton_4.setText(_translate("Form", "Дискреты"))
