# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\modbus_rtu_discrets.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp

class Ui_Form(object):
    def setupUi(self, Form, processingObject):
        self.processingObject = processingObject
        self.asdu = processingObject.asdu
        self.device = self.asdu.interfaces[processingObject.processingInterfaceIndex].protocols[processingObject.processingProtocolIndex].devices[processingObject.processingDeviceIndex]

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
        self.frame_8.setGeometry(QtCore.QRect(0, 0, 1357, 40))
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

    def closeEvent(self, event, obj):
        obj.cancel()

    def resizeEvent(self, event):
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, self.form.rect().width(), self.form.rect().height() - 100))
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, self.form.rect().width(), self.form.rect().height() - 100))

    def settingsRender(self):
        _translate = QtCore.QCoreApplication.translate
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, self.form.rect().width(), self.form.rect().height() - 100))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMinimumSize(QtCore.QSize(1366, 984))
        self.groupBox.setStyleSheet("QGroupBox { border: none; }")
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.frame_9 = QtWidgets.QFrame(self.groupBox)
        self.frame_9.setGeometry(QtCore.QRect(40, 27, 380, 135))
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
        self.frame_16.setGeometry(QtCore.QRect(0, 65, 245, 70))
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
        self.startingAddress = QtWidgets.QLineEdit(self.frame_16)
        self.startingAddress.setGeometry(QtCore.QRect(0, 40, 245, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startingAddress.setFont(font)
        self.startingAddress.setStyleSheet("QLineEdit { border: 1px solid #999; }")
        self.startingAddress.setObjectName("startingAddress")
        self.startingAddress.setValidator(QIntValidator(self.frame_16))
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(40, 200, 602, 632))
        self.tableWidget.setStyleSheet("QTableWidget { border: 1px solid #777; }\n"
"QTableWidget QHeaderView { border: none; }\n"
"QTableWidget, QTableWidget QHeaderView:section, QTableWidget QHeaderView {\n"
"     background-color: #e5e5e5; \n"
"}\n"
"QHeaderView::section { border: 1px solid #aaa; }")
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideLeft)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(int(self.device.data["discrets"]["rowsCount"]))
        self.tableWidget.setColumnCount(int(self.device.data["discrets"]["columnCount"]))
        self.tableWidget.setObjectName("tableWidget")

        for i in range(int(self.device.data["discrets"]["rowsCount"])):
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
        
        for i in range(int(self.device.data["discrets"]["columnCount"])):
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(11)
            item.setFont(font)
            if "column_%d" % (i + 1) in self.device.data["discrets"]:
                item.setText(_translate("Form", self.device.columnNames["discrets"]["column_%d" % (i + 1)]))
            self.tableWidget.setHorizontalHeaderItem(i, item)
        
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)

        for i in range(int(self.device.data["discrets"]["columnCount"])):
            for j in range(int(self.device.data["discrets"]["rowsCount"])):
                item = QtWidgets.QTableWidgetItem()
                font = QtGui.QFont()
                font.setPointSize(11)
                item.setFont(font)
                item.setBackground(QtGui.QColor(0, 0, 0, 0))
                if "column_%d" % (i + 1) in self.device.data["discrets"]:
                    item.setText(self.device.data["discrets"]["column_%d" % (i + 1)].get("row_%d" % (j + 1)))
                
                self.tableWidget.setItem(j, i, item)
        self.tableWidget.itemChanged.connect(self.updateDeviceTableSetting)

        self.frame_3 = QtWidgets.QFrame(self.groupBox)
        self.frame_3.setGeometry(QtCore.QRect(700, 200, 155, 181))
        self.frame_3.setStyleSheet("QFrame { border: none; }")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        # self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        # self.pushButton_4.setGeometry(QtCore.QRect(0, 0, 155, 35))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.pushButton_4.setFont(font)
        # self.pushButton_4.setStyleSheet("QPushButton { border-radius: 5px; background-color: #FED2AA; }")
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.pushButton_7 = QtWidgets.QPushButton(self.frame_3)
        # self.pushButton_7.setGeometry(QtCore.QRect(0, 92, 155, 35))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.pushButton_7.setFont(font)
        # self.pushButton_7.setStyleSheet("QPushButton { border-radius: 5px; background-color: #FED2AA; }")
        # self.pushButton_7.setObjectName("pushButton_7")
        # self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        # self.pushButton_5.setGeometry(QtCore.QRect(0, 46, 155, 35))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.pushButton_5.setFont(font)
        # self.pushButton_5.setStyleSheet("QPushButton { border-radius: 5px; background-color: #FED2AA; }")
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        # self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        # self.pushButton_6.setGeometry(QtCore.QRect(0, 138, 155, 35))
        # font = QtGui.QFont()
        # font.setPointSize(11)
        # self.pushButton_6.setFont(font)
        # self.pushButton_6.setStyleSheet("QPushButton { border-radius: 5px; background-color: #FED2AA; }")
        # self.pushButton_6.setObjectName("pushButton_6")
        # self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.label_8.setText(_translate("Form", "MODBUS RTU (%s)" % (self.device.name)))
        self.label_15.setText(_translate("Form", "Начальный адрес:"))
        self.save.setText(_translate("Form", "Сохранить"))
        # self.pushButton_4.setText(_translate("Form", "Добавить"))
        # self.pushButton_7.setText(_translate("Form", "Удалить"))
        # self.pushButton_5.setText(_translate("Form", "Создать дубликат"))
        # self.pushButton_6.setText(_translate("Form", "По умолчанию"))
        self.cancel.setText(_translate("Form", "Отмена"))
        self.verticalLayout.addWidget(self.groupBox)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.startingAddress.setText(self.device.settings.get("discrets_startingAddress"))
        self.startingAddress.editingFinished.connect(lambda: self.updateDeviceText("startingAddress", "discrets_startingAddress"))

    def updateDeviceText(self, button, prop):
        self.device.settings[prop] = getattr(self, button).text()

    def updateDeviceTableSetting(self, item):
        i = item.row()
        j = item.column()
        if not "column_%d" % (j + 1) in self.device.data["discrets"]:
            self.device.data["discrets"]["column_%d" % j] = dict()
        
        self.device.data["discrets"]["column_%d" % (j + 1)]["row_%d" % (i + 1)] = item.text()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", self.device.name))
        self.pushButton.setText(_translate("Form", "Настройки"))
        self.pushButton_2.setText(_translate("Form", "Регистры"))
        self.pushButton_8.setText(_translate("Form", "Дискреты"))
