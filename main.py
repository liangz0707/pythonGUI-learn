import sys
from PyQt4 import QtCore,QtGui
from mainframe_ui import Ui_myfr as m_ui

class myfr(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = m_ui()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.setText)

    def setText(self):
        self.ui.label.setText("aaaaaaaaaaa")
        print "   aqsdas"


app = QtGui.QApplication(sys.argv)
myapp = myfr()
myapp.show()
sys.exit(app.exec_())