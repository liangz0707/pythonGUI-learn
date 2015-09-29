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

class Ui_myediter(object):
    def setupUi(self, myediter):
        myediter.setObjectName(_fromUtf8("myediter"))
        myediter.resize(467, 470)
        self.verticalLayout = QtGui.QVBoxLayout(myediter)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.widget = QtGui.QWidget(myediter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.openBut = QtGui.QPushButton(self.widget)
        self.openBut.setObjectName(_fromUtf8("openBut"))
        self.horizontalLayout.addWidget(self.openBut)
        self.saveBut = QtGui.QPushButton(self.widget)
        self.saveBut.setObjectName(_fromUtf8("saveBut"))
        self.horizontalLayout.addWidget(self.saveBut)
        self.closeBut = QtGui.QPushButton(self.widget)
        self.closeBut.setObjectName(_fromUtf8("closeBut"))
        self.horizontalLayout.addWidget(self.closeBut)
        self.verticalLayout.addWidget(self.widget)
        self.textEdit = QtGui.QTextEdit(myediter)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout.addWidget(self.textEdit)

        self.retranslateUi(myediter)
        QtCore.QMetaObject.connectSlotsByName(myediter)

    def retranslateUi(self, myediter):
        myediter.setWindowTitle(_translate("myediter", "文本编辑器", None))
        self.openBut.setText(_translate("myediter", "打开", None))
        self.saveBut.setText(_translate("myediter", "保存", None))
        self.closeBut.setText(_translate("myediter", "关闭", None))

