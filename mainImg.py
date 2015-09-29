# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore,QtGui
from Mainwindow_ui import Ui_MainWindow as main_ui
from ImageDlg_ui import Ui_ImageDlg as imgDlg_ui
from LeftWidget_ui import Ui_LeftWidget as L_ui
from TopWidget_ui import Ui_TopWidget as T_ui
from pyqtgraph.Qt import QtGui, QtCore


class myediter(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = main_ui()
        self.ui.setupUi(self)

        cenW = QtGui.QWidget(self)
        topW = QtGui.QWidget(self)
        leftW = QtGui.QWidget(self)

        self.setCentralWidget(cenW)
        self.ui.leftDockW.setWidget(leftW)
        self.ui.TopDockW.setWidget(topW)

        cenW.ui = imgDlg_ui()
        cenW.ui.setupUi(cenW)
        self.cui = cenW.ui

        leftW.ui = L_ui()
        leftW.ui.setupUi(leftW)
        self.lui = leftW.ui

        topW.ui = T_ui()
        topW.ui.setupUi(topW)
        self.tui = cenW.ui

        QtCore.QObject.connect(self.lui.openButton,QtCore.SIGNAL("clicked()"),self.openImg)


    def openImg(self):
        from scipy import misc
        l = misc.lena()
        misc.imshow(l)

app = QtGui.QApplication(sys.argv)
myapp = myediter()
myapp.show()
sys.exit(app.exec_())
