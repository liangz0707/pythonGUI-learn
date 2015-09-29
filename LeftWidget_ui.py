# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LeftWidget.ui'
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

class Ui_LeftWidget(object):
    def setupUi(self, LeftWidget):
        LeftWidget.setObjectName(_fromUtf8("LeftWidget"))
        LeftWidget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(LeftWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.openButton = QtGui.QPushButton(LeftWidget)
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.verticalLayout.addWidget(self.openButton)

        self.retranslateUi(LeftWidget)
        QtCore.QMetaObject.connectSlotsByName(LeftWidget)

    def retranslateUi(self, LeftWidget):
        LeftWidget.setWindowTitle(_translate("LeftWidget", "左侧悬浮", None))
        self.openButton.setText(_translate("LeftWidget", "打开", None))

