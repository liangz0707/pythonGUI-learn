# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore,QtGui
from mainframe_ui import Ui_myediter as m_ui

class myediter(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = m_ui()
        self.ui.setupUi(self)
        self.ui.saveBut.setEnabled(False)

        QtCore.QObject.connect(self.ui.openBut,QtCore.SIGNAL("clicked()"),self.openFile)
        QtCore.QObject.connect(self.ui.saveBut,QtCore.SIGNAL("clicked()"),self.saveFile)
        QtCore.QObject.connect(self.ui.closeBut,QtCore.SIGNAL("clicked()"),self.close)

    def openFile(self):
        qf = QtGui.QFileDialog(self)
        #下面三行用于解决中文编码问题
        self.fileName = str(qf.getOpenFileName(None).toLocal8Bit())
        self.fileName = unicode(self.fileName,'gbk','ignore')
        print (self.fileName)
        self.ui.saveBut.setEnabled(True)
        import codecs
        s = codecs.open(self.fileName,'rb',"utf-8").read()
        self.ui.textEdit.setPlainText(s)

    def saveFile(self):
        from os.path import isfile
        if isfile(self.fileName):
            import codecs
            s = codecs.open(self.fileName,'w','utf-8')
            s.write(unicode(self.ui.textEdit.toPlainText()))
            s.close()
            print("ok")


app = QtGui.QApplication(sys.argv)
myapp = myediter()
myapp.show()
sys.exit(app.exec_())

'''
    1. 关于中文编码的解释
    QString 必须接受unicode编码的字符串
    s = QtCore.QString('中文') 出错,这个传入的是byte类型的字符串，在python3中这是unicode
    s = QtCore.QString(u'中文') 正确
    2，Qt 中的 QByteArray 等同于 Python 中的 bytes 格式字符串
    在 PyQt 中，QString.toLocal8Bit() 返回一个 QByteArray 对象。
    而 print b 能够正确显示 str(b) 就可以将 b 转换成 Python 字符串。
    3.str只接受ascii编码的字符串
'''