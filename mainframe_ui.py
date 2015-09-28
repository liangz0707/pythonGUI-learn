# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainframe.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_myfr(object):
    def setupUi(self, myfr):
        myfr.setObjectName(_fromUtf8("myfr"))
        myfr.resize(848, 478)
        self.horizontalLayout = QtGui.QHBoxLayout(myfr)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(myfr)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.listWidget = QtGui.QListWidget(self.widget)
        self.listWidget.setGeometry(QtCore.QRect(430, 120, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setGeometry(QtCore.QRect(230, 120, 71, 16))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.toolButton = QtGui.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(240, 60, 37, 18))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(120, 190, 261, 121))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 40, 141, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(myfr)
        QtCore.QMetaObject.connectSlotsByName(myfr)

    def retranslateUi(self, myfr):
        myfr.setWindowTitle(_translate("myfr", "Form", None))
        self.checkBox.setText(_translate("myfr", "CheckBox", None))
        self.toolButton.setText(_translate("myfr", "...", None))
        self.label.setText(_translate("myfr", "TextLabel", None))
        self.pushButton.setText(_translate("myfr", "&Load Image", None))

