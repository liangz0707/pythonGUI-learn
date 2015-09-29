# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TopWidget.ui'
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

class Ui_TopWidget(object):
    def setupUi(self, TopWidget):
        TopWidget.setObjectName(_fromUtf8("TopWidget"))
        TopWidget.resize(400, 300)
        self.horizontalLayout = QtGui.QHBoxLayout(TopWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton = QtGui.QPushButton(TopWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(TopWidget)
        QtCore.QMetaObject.connectSlotsByName(TopWidget)

    def retranslateUi(self, TopWidget):
        TopWidget.setWindowTitle(_translate("TopWidget", "顶部悬浮", None))
        self.pushButton.setText(_translate("TopWidget", "PushButton", None))

