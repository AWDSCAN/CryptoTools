# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KEY_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KEY1(object):
    def setupUi(self, KEY1):
        KEY1.setObjectName("KEY1")
        KEY1.resize(530, 65)
        self.gridLayout = QtWidgets.QGridLayout(KEY1)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(KEY1)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.key = QtWidgets.QLineEdit(KEY1)
        self.key.setObjectName("key")
        self.horizontalLayout.addWidget(self.key)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.keyenter = QtWidgets.QPushButton(KEY1)
        self.keyenter.setObjectName("keyenter")
        self.gridLayout.addWidget(self.keyenter, 0, 1, 1, 1)

        self.retranslateUi(KEY1)
        QtCore.QMetaObject.connectSlotsByName(KEY1)
        KEY1.setTabOrder(self.key, self.keyenter)

    def retranslateUi(self, KEY1):
        _translate = QtCore.QCoreApplication.translate
        KEY1.setWindowTitle(_translate("KEY1", "Key"))
        self.label.setText(_translate("KEY1", "Key"))
        self.keyenter.setText(_translate("KEY1", "确定"))