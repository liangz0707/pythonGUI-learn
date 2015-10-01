# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/TopWidget.ui'
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
        TopWidget.resize(583, 101)
        self.horizontalLayout = QtGui.QHBoxLayout(TopWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tabWidget = QtGui.QTabWidget(TopWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.tab_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.tab_3)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtGui.QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.createSCdicButton = QtGui.QPushButton(self.tab_3)
        self.createSCdicButton.setObjectName(_fromUtf8("createSCdicButton"))
        self.horizontalLayout_2.addWidget(self.createSCdicButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(TopWidget)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(TopWidget)

    def retranslateUi(self, TopWidget):
        TopWidget.setWindowTitle(_translate("TopWidget", "顶部悬浮", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("TopWidget", "特征点提取", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("TopWidget", "深度学习", None))
        self.label.setText(_translate("TopWidget", "基的个数", None))
        self.createSCdicButton.setText(_translate("TopWidget", "生成字典", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("TopWidget", "稀疏编码", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("TopWidget", "Theano", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("TopWidget", "None", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("TopWidget", "None", None))

