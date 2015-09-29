# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageDlg.ui'
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
        ImageDlg.resize(791, 509)
        self.gridLayout = QtGui.QGridLayout(ImageDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.matW = MatplotlibWidget(ImageDlg)
        self.matW.setObjectName(_fromUtf8("matW"))
        self.gridLayout.addWidget(self.matW, 0, 0, 1, 1)

        self.retranslateUi(ImageDlg)
        QtCore.QMetaObject.connectSlotsByName(ImageDlg)

    def retranslateUi(self, ImageDlg):
        ImageDlg.setWindowTitle(_translate("ImageDlg", "CenterFW", None))

from matplotlibwidget import MatplotlibWidget
