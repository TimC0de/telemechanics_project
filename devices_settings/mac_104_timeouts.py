# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\mac_104_timeouts.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def getDevice(self):
        if self.processingObject.processTcpClient:
            return self.asdu.tcpClients[self.processingObject.processingTcpClientIndex]
        else:
            return self.asdu.interfaces[self.processingObject.processingInterfaceIndex].protocols[self.processingObject.processingProtocolIndex].devices[self.processingObject.processingDeviceIndex]
    
    def setupUi(self, Form, processingObject):
        self.processingObject = processingObject
        self.asdu = processingObject.asdu
        self.device = self.getDevice()

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
        self.scrollArea.setMinimumSize(QtCore.QSize(1366, 728))
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
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
        self.pushButton.setStyleSheet("QPushButton { border: none; border-top-left-radius: 5px; border-top-right-radius: 5px; background-color: transparent; }")
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
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_8.setGeometry(QtCore.QRect(320, 10, 140, 30))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet("QPushButton { border: none; border-top-left-radius: 5px; border-top-right-radius: 5px; }")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.timeoutsRender()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def timeoutsRender(self):
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1366, 728))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(1366, 715))
        self.groupBox.setStyleSheet("QGroupBox { border: none; }")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.frame_9 = QtWidgets.QFrame(self.groupBox)
        self.frame_9.setGeometry(QtCore.QRect(40, 67, 380, 401))
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
        self.frame_16.setGeometry(QtCore.QRect(0, 160, 245, 70))
        self.frame_16.setStyleSheet("QFrame { border: none; }")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_15 = QtWidgets.QLabel(self.frame_16)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 245, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.t1 = QtWidgets.QLineEdit(self.frame_16)
        self.t1.setGeometry(QtCore.QRect(0, 40, 245, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t1.setFont(font)
        self.t1.setStyleSheet("QLineEdit { border: 1px solid #999; }")
        self.t1.setObjectName("t1")
        self.frame_17 = QtWidgets.QFrame(self.frame_9)
        self.frame_17.setGeometry(QtCore.QRect(0, 230, 245, 70))
        self.frame_17.setStyleSheet("QFrame { border: none; }")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.label_16 = QtWidgets.QLabel(self.frame_17)
        self.label_16.setGeometry(QtCore.QRect(0, 0, 245, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.t2 = QtWidgets.QLineEdit(self.frame_17)
        self.t2.setGeometry(QtCore.QRect(0, 40, 245, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t2.setFont(font)
        self.t2.setStyleSheet("QLineEdit { border: 1px solid #999; }")
        self.t2.setObjectName("t2")
        self.frame_18 = QtWidgets.QFrame(self.frame_9)
        self.frame_18.setGeometry(QtCore.QRect(0, 300, 245, 70))
        self.frame_18.setStyleSheet("QFrame { border: none; }")
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_17 = QtWidgets.QLabel(self.frame_18)
        self.label_17.setGeometry(QtCore.QRect(0, 0, 245, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.t3 = QtWidgets.QLineEdit(self.frame_18)
        self.t3.setGeometry(QtCore.QRect(0, 40, 245, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.t3.setFont(font)
        self.t3.setStyleSheet("QLineEdit { border: 1px solid #999; }")
        self.t3.setObjectName("lineEdit_3")
        self.frame = QtWidgets.QFrame(self.frame_9)
        self.frame.setGeometry(QtCore.QRect(0, 80, 245, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 0, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.frame_9)
        self.frame_2.setGeometry(QtCore.QRect(0, 120, 245, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(90, 0, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
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

        for tEdit in ["t1", "t2", "t3"]:
            getattr(self, tEdit).setText(self.device.settings.get(tEdit))
            getattr(self, tEdit).editingFinished.connect(self.editionCallback(tEdit))

    def editionCallback(self, field):
        return lambda: self.updateDeviceText(field)

    def updateDeviceText(self, field):
        self.device.settings[field] = getattr(self, field).text()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.device.name))
        self.pushButton.setText(_translate("Form", "Настройки"))
        self.pushButton_2.setText(_translate("Form", "Данные"))
        self.pushButton_8.setText(_translate("Form", "Тайм-ауты"))
        self.label_8.setText(_translate("Form", "МЭК 104 (%s)" % (self.device.name)))
        self.label_15.setText(_translate("Form", "t1,с:"))
        self.label_16.setText(_translate("Form", "t2,с:"))
        self.label_17.setText(_translate("Form", "t3,с:"))
        self.label.setText(_translate("Form", "К"))
        self.label_2.setText(_translate("Form", "1"))
        self.label_3.setText(_translate("Form", "W"))
        self.label_4.setText(_translate("Form", "1"))
        self.save.setText(_translate("Form", "Сохранить"))
        self.cancel.setText(_translate("Form", "Отмена"))