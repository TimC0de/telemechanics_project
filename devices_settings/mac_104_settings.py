# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mac_104.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class Ui_Form(object):

    def getDevice(self):
        if self.processingObject.processTcpClient:
            return self.td.tcpClients[self.processingObject.processingTcpClientIndex]
        else:
            return self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.processingObject.processingProtocolIndex].devices[self.processingObject.processingDeviceIndex]
    
    def setupUi(self, Form, processingObject):
        self.processingObject = processingObject
        self.td = processingObject.td
        self.asdu = processingObject.asdu
        self.device = self.getDevice()
        self.ipRegExp = QRegExp("(\\d{1,3}\\.){3}\\d{1,3}")

        Form.setObjectName("Form")
        font = QtGui.QFont()
        font.setPointSize(8)
        Form.setFont(font)
        Form.setStyleSheet("QWidget {\n"
"    background-color: white;\n"
"}")
        Form.resizeEvent = lambda event: self.resizeEvent(event)
        Form.closeEvent = lambda event: self.closeEvent(event, self.asdu)
        self.form = Form
        self.frame_8 = QtWidgets.QFrame(Form)
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 1440, 40))
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
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, self.form.rect().width(), self.form.rect().height() - 100))
        self.scrollArea.setMinimumSize(QtCore.QSize(1366, 728))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.save = QtWidgets.QPushButton(Form)
        self.save.setGeometry(QtCore.QRect(1000, 50, 155, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.save.setFont(font)
        self.save.setStyleSheet("QPushButton { border-radius: 5px; background-color: #FED2AA; }")
        self.save.setObjectName("save")
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setGeometry(QtCore.QRect(800, 50, 155, 35))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("QPushButton { border-radius: 5px; background-color: #C4C4C4; }")
        self.cancel.setObjectName("cancel")
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.settingsRender()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def settingsRender(self):
        _translate = QtCore.QCoreApplication.translate
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, self.form.rect().width(), self.form.rect().height() - 100))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(1366, 710))
        self.groupBox.setStyleSheet("QGroupBox { border: none; }")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(40, 245, 1360, 2))
        self.line.setStyleSheet("Line {\n"
"    border: none;\n"
"    background-color: #c4c4c4;\n"
"}")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.frame_9 = QtWidgets.QFrame(self.groupBox)
        self.frame_9.setGeometry(QtCore.QRect(40, 27, 380, 200))
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
        self.frame_16.setGeometry(QtCore.QRect(0, 75, 200, 70))
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
        self.asduAddress = QtWidgets.QLineEdit(self.frame_16)
        self.asduAddress.setGeometry(QtCore.QRect(0, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.asduAddress.setFont(font)
        self.asduAddress.setStyleSheet("QLineEdit { border: 1px solid #aaaaaa; }")
        self.asduAddress.setObjectName("asduAddress")
        self.frame_24 = QtWidgets.QFrame(self.frame_9)
        self.frame_24.setGeometry(QtCore.QRect(0, 160, 300, 40))
        self.frame_24.setStyleSheet("QFrame { border: none; }")
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.allowSync = QtWidgets.QCheckBox(self.frame_24)
        self.allowSync.setGeometry(QtCore.QRect(0, 0, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.allowSync.setFont(font)
        self.allowSync.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.allowSync.setObjectName("allowSync")
        self.frame_10 = QtWidgets.QFrame(self.groupBox)
        self.frame_10.setGeometry(QtCore.QRect(40, 250, 531, 150))
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
        self.frame_11 = QtWidgets.QFrame(self.groupBox)
        self.frame_11.setGeometry(QtCore.QRect(712, 250, 531, 150))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_10 = QtWidgets.QLabel(self.frame_11)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 380, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.frame_27 = QtWidgets.QFrame(self.frame_11)
        self.frame_27.setGeometry(QtCore.QRect(0, 110, 531, 40))
        self.frame_27.setStyleSheet("QFrame { border: none; }")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.transferDatetime = QtWidgets.QCheckBox(self.frame_27)
        self.transferDatetime.setGeometry(QtCore.QRect(0, 0, 531, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.transferDatetime.setFont(font)
        self.transferDatetime.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.transferDatetime.setObjectName("transferDatetime")
        self.frame_28 = QtWidgets.QFrame(self.frame_11)
        self.frame_28.setGeometry(QtCore.QRect(0, 60, 300, 40))
        self.frame_28.setStyleSheet("QFrame { border: none; }")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.sporadic = QtWidgets.QCheckBox(self.frame_28)
        self.sporadic.setGeometry(QtCore.QRect(0, 0, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.sporadic.setFont(font)
        self.sporadic.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.sporadic.setObjectName("sporadic")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(40, 435, 1360, 2))
        self.line_2.setStyleSheet("Line {\n"
"    border: none;\n"
"    background-color: #c4c4c4;\n"
"}")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.frame_12 = QtWidgets.QFrame(self.groupBox)
        self.frame_12.setGeometry(QtCore.QRect(712, 440, 531, 160))
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.label_11 = QtWidgets.QLabel(self.frame_12)
        self.label_11.setGeometry(QtCore.QRect(0, 0, 380, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.frame_29 = QtWidgets.QFrame(self.frame_12)
        self.frame_29.setGeometry(QtCore.QRect(0, 120, 531, 40))
        self.frame_29.setStyleSheet("QFrame { border: none; }")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.actualityChangeTrigger = QtWidgets.QCheckBox(self.frame_29)
        self.actualityChangeTrigger.setGeometry(QtCore.QRect(0, 0, 531, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.actualityChangeTrigger.setFont(font)
        self.actualityChangeTrigger.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.actualityChangeTrigger.setObjectName("actualityChangeTrigger")
        self.frame_17 = QtWidgets.QFrame(self.frame_12)
        self.frame_17.setGeometry(QtCore.QRect(0, 50, 200, 70))
        self.frame_17.setStyleSheet("QFrame { border: none; }")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_16 = QtWidgets.QLabel(self.frame_17)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.period = QtWidgets.QLineEdit(self.frame_17)
        self.period.setGeometry(QtCore.QRect(0, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.period.setFont(font)
        self.period.setStyleSheet("QLineEdit { border: 1px solid #aaaaaa; }")
        self.period.setObjectName("period")
        self.frame_13 = QtWidgets.QFrame(self.groupBox)
        self.frame_13.setGeometry(QtCore.QRect(40, 440, 531, 160))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_12 = QtWidgets.QLabel(self.frame_13)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 380, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.frame_31 = QtWidgets.QFrame(self.frame_13)
        self.frame_31.setGeometry(QtCore.QRect(0, 110, 531, 40))
        self.frame_31.setStyleSheet("QFrame { border: none; }")
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.bitNT = QtWidgets.QCheckBox(self.frame_31)
        self.bitNT.setGeometry(QtCore.QRect(0, 0, 531, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bitNT.setFont(font)
        self.bitNT.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.bitNT.setObjectName("bitNT")
        self.frame_32 = QtWidgets.QFrame(self.frame_13)
        self.frame_32.setGeometry(QtCore.QRect(0, 60, 300, 40))
        self.frame_32.setStyleSheet("QFrame { border: none; }")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.bit4 = QtWidgets.QCheckBox(self.frame_32)
        self.bit4.setGeometry(QtCore.QRect(0, 0, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.bit4.setFont(font)
        self.bit4.setStyleSheet("QCheckBox { border: none; background-color: transparent; }")
        self.bit4.setObjectName("bit4")
        self.frame_15 = QtWidgets.QFrame(self.groupBox)
        self.frame_15.setGeometry(QtCore.QRect(712, 27, 531, 200))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_14 = QtWidgets.QLabel(self.frame_15)
        self.label_14.setGeometry(QtCore.QRect(0, 0, 380, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.frame_18 = QtWidgets.QFrame(self.frame_15)
        self.frame_18.setGeometry(QtCore.QRect(0, 50, 200, 70))
        self.frame_18.setStyleSheet("QFrame { border: none; }")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_17 = QtWidgets.QLabel(self.frame_18)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.ipAddress = QtWidgets.QLineEdit(self.frame_18)
        self.ipAddress.setGeometry(QtCore.QRect(0, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ipAddress.setFont(font)
        self.ipAddress.setStyleSheet("QLineEdit { border: 1px solid #aaaaaa; }")
        self.ipAddress.setObjectName("ipAddress")
        self.frame_19 = QtWidgets.QFrame(self.frame_15)
        self.frame_19.setGeometry(QtCore.QRect(0, 130, 200, 70))
        self.frame_19.setStyleSheet("QFrame { border: none; }")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.label_18 = QtWidgets.QLabel(self.frame_19)
        self.label_18.setGeometry(QtCore.QRect(0, 0, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.port = QtWidgets.QLineEdit(self.frame_19)
        self.port.setGeometry(QtCore.QRect(0, 40, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.port.setFont(font)
        self.port.setStyleSheet("QLineEdit { border: 1px solid #aaaaaa; }")
        self.port.setObjectName("port")

        self.verticalLayout.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.label_8.setText(_translate("Form", "МЭК 104 (%s)" % (self.device.name)))
        self.label_15.setText(_translate("Form", "Общий адрес ASDU:"))
        self.allowSync.setText(_translate("Form", "Разрешить синхронизацию"))
        self.label_9.setText(_translate("Form", "Тип данных"))
        self.fixedData.setText(_translate("Form", "Фиксированные данные(Без необходимости не включать)"))
        self.fastChanges.setText(_translate("Form", "Быстрые изменения"))
        self.label_10.setText(_translate("Form", "Передача данных"))
        self.transferDatetime.setText(_translate("Form", "Передавать метку времени каждые 10 минут"))
        self.sporadic.setText(_translate("Form", "Спорадическая"))
        self.label_11.setText(_translate("Form", "Фоновое сканирование"))
        self.actualityChangeTrigger.setText(_translate("Form", "Срабатывание при изменении актуальности"))
        self.label_16.setText(_translate("Form", "Период, c:"))
        self.label_12.setText(_translate("Form", "Признаки описателя качества"))
        self.bitNT.setText(_translate("Form", "Бит NT"))
        self.bit4.setText(_translate("Form", "Бит 4"))
        self.save.setText(_translate("Form", "Сохранить"))
        self.label_14.setText(_translate("Form", "Фоновое сканирование"))
        self.label_17.setText(_translate("Form", "IP-адрес:"))
        self.label_18.setText(_translate("Form", "Порт:"))
        self.cancel.setText(_translate("Form", "Отмена"))

        keyTypes = {"asduAddress": "text",
         "allowSync": "boolean",
          "ipAddress": "text",
           "port": "text",
            "fastChanges": "boolean",
             "fixedData": "boolean",
              "sporadic": "boolean",
               "transferDatetime": "boolean",
                "bitNT": "boolean",
                 "bit4": "boolean",
                  "period": "text",
                   "actualityChangeTrigger": "boolean"}

        for key in keyTypes:
                if keyTypes[key] == "text":
                        if key == 'ipAddress':
                            getattr(self, key).setValidator(QRegExpValidator(self.ipRegExp, getattr(self, key).parent()))
                        else:
                            getattr(self, key).setValidator(QIntValidator(getattr(self, key)))
                        
                        getattr(self, key).setText(self.device.settings.get(key))
                        getattr(self, key).editingFinished.connect(self.editionCallback(key))
                else:
                        getattr(self, key).setChecked(self.device.settings.get(key) or False)
                        getattr(self, key).stateChanged.connect(self.checkCallback(key))

    def closeEvent(self, event, obj):
        obj.cancel()

    def resizeEvent(self, event):
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, self.form.rect().width(), self.form.rect().height() - 100))
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, self.form.rect().width(), self.form.rect().height() - 100))

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
        self.pushButton_2.setText(_translate("Form", "Данные"))
        self.pushButton_4.setText(_translate("Form", "Тайм-ауты"))
