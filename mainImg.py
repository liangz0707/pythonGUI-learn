# -*- coding: utf-8 -*-
import sys
import numpy as np
import random
from skimage import io
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.misc.pilutil import  toimage
from PIL.ImageQt import ImageQt
#该方法把nparray的数组转化成了Qt所需要的类型
def nparrayToQPixmap(arrayImage):
    pilImage = toimage(arrayImage)
    qtImage = ImageQt(pilImage)
    qImage = QtGui.QImage(qtImage).convertToFormat(QtGui.QImage.Format_ARGB32)
    qPixmap = QtGui.QPixmap(qImage)
    return qPixmap
import math
from pyqtgraph.Qt import QtGui, QtCore
import SpraseCoding.sparse_coding as sc

from ui.mainWindow_ui import Ui_MainWindow as main_ui
from ui.ImageDlg_ui import Ui_ImageDlg as imgDlg_ui
from ui.LeftWidget_ui import Ui_LeftWidget as L_ui
from ui.TopWidget_ui import Ui_TopWidget as T_ui
#组织窗口布局
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
        self.ui.topDockW.setWidget(topW)

        cenW.ui = imgDlg_ui()
        cenW.ui.setupUi(cenW)
        self.cui = cenW.ui

        leftW.ui = L_ui()
        leftW.ui.setupUi(leftW)
        self.lui = leftW.ui

        topW.ui = T_ui()
        topW.ui.setupUi(topW)
        self.tui = topW.ui

        QtCore.QObject.connect(self.lui.openButton,QtCore.SIGNAL("clicked()"),self.openImg)
        #生成字典
        QtCore.QObject.connect(self.tui.createSCdicButton,QtCore.SIGNAL("clicked()"),self.createDict)
    #选择几个图片文件，然后创建字典
    def createDict(self):
        '''
        以下方法提供了对于numpy和PIL之间的数据转换
            asarray(im1)
            Image.fromarray(addition)
        '''
        patchNum = 4 #每张图片要提取patch的个数
        patchSize =8 #每张图片需要提取patch的尺寸
        imgList = QtGui.QFileDialog.getOpenFileNames(self)
        #print (imgList.len())
        patchList = [] #用于存放向量花的patch
        for i in imgList:
            fileName = str(i.toLocal8Bit())
            fName = unicode(fileName,'gbk','ignore')
            fName#读取这个图片，并且提取patch
            c = io.imread(fName)
            #print(type(c),c.shape)
            for j in xrange(patchNum):
                y,x = [random.randint(0,c.shape[d]-patchSize) for d in [0,1]]  #从这个尺寸当中抽取出所需要随机patch
                p = c[y:y+patchSize,x:x+patchSize,0].reshape(patchSize**2,1) #由于是三通道图像，所以先使用一个通道进行测试
                #print type(p),p.shape
                patchList.append(p)
        X = np.hstack(patchList)
        X = np.asarray(X,dtype='float')
        print (X.dtype,X.shape) #生成了我们想要的样本

        print u"开始计算字典ing"
        (B,S) = sc.sparse_coding(X,64,0.4,1)
        self.callback(X, B, S)

    def openImg(self):
        from scipy import misc
        l = misc.lena()
        print l.shape
        nparrayToQPixmap(l)
        self.cui.imgLabel.setPixmap(nparrayToQPixmap(l))
    def callback(self,X, B, S):
        plt.subplot(2, 2, 1)
        self.visualize_patches(X)
        plt.title("originals")
        plt.subplot(2, 2, 2)
        self.visualize_patches(B)
        plt.title("bases")
        plt.subplot(2, 2, 3)
        self.visualize_patches(np.dot(B, S))
        plt.title("reconstructions")
        plt.subplot(2, 2, 4)
        self.visualize_patches(X - np.dot(B, S))
        plt.title("differences")
        plt.show()
    def visualize_patches(self,B):
        # assume square
        mpatch = int(math.floor(math.sqrt(B.shape[0])))
        npatch = mpatch

        m = int(math.floor(math.sqrt(B.shape[1])))
        n = int(math.ceil(B.shape[1] * 1.0 / m))
        collage = np.zeros((m*mpatch, n*npatch))
        for i in xrange(m):
            for j in xrange(n):
                try:
                    patch = B[:, i*n + j]
                except IndexError:
                    continue
                patch = self.onto_unit(patch.reshape((mpatch, npatch)))
                collage[i*mpatch:(i+1)*mpatch, j*npatch:(j+1)*npatch] = patch
        plt.imshow(collage, cmap=cm.gray)
    def onto_unit(self,x):
        a = np.min(x)
        b = np.max(x)
        return (x - a) / (b - a)

app = QtGui.QApplication(sys.argv)
myapp = myediter()
myapp.show()
sys.exit(app.exec_())
