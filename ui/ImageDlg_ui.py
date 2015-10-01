# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ImageDlg.ui'
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

class Ui_ImageDlg(object):
    def setupUi(self, ImageDlg):
        ImageDlg.setObjectName(_fromUtf8("ImageDlg"))
        ImageDlg.resize(480, 331)
        self.gridLayout = QtGui.QGridLayout(ImageDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.imgLabel = QtGui.QLabel(ImageDlg)
        self.imgLabel.setText(_fromUtf8(""))
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setObjectName(_fromUtf8("imgLabel"))
        self.gridLayout.addWidget(self.imgLabel, 0, 0, 1, 1)

        self.retranslateUi(ImageDlg)
        QtCore.QMetaObject.connectSlotsByName(ImageDlg)

    def retranslateUi(self, ImageDlg):
        ImageDlg.setWindowTitle(_translate("ImageDlg", "CenterFW", None))

