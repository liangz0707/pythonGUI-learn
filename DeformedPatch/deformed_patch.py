# -*- coding: utf-8 -*-
__author__ = 'Zhe'
import theano
import numpy as np
import theano.tensor as T
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from skimage import io
import skimage
from theano.tensor.nnet import conv #接触theano进行卷积操作
import time
from pylab import mpl
'''
输入两个patch，返回变形的（u,v）向量
'''
#解决matlibplot当中中文显示问题
mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体

#这里并非优化W而是优化(u,v)
class deformed_patch(object):
    def __init__(self):
        pass

    def getXYGrad(self,input):
        ylen = input.shape[0]
        xlen = input.shape[1]
        #这个输入需要改变成一维的，为了借助Theano的函数
        src = T.dmatrix() #定义输入图像数组 二维、单通道

        #这个滤波器
        filter_shape = np.asarray([2,1,2,2],dtype='int')
        image_shape = np.asarray([1,1,ylen,xlen],dtype='int') #就是实际图像的大小

        #从src向dst变化
        src = src.reshape((1, 1, ylen, xlen))

        #计算两个方向的梯度
        Wx=np.asarray([[1,-1],[0,0]],dtype='float64') #结果是W+Wx
        Wy=np.asarray([[1,0],[-1,0]],dtype='float64') #
        W=np.zeros(filter_shape)
        W[0,0]=Wx
        W[1,0]=Wy
        #print W.shape
        #print filter_shape.shape
        #print image_shape.shape
        #首先需要计算梯度
        src_xd = conv.conv2d(
                input=src,
                filters=W,
                filter_shape=filter_shape,
                image_shape=image_shape
            )#卷积会忽略边界

        getGradXY = theano.function([src],src_xd)

        #input = [[1,1,1,1,1,1,1],[2,2,2,2,2,2,2],[3,3,3,3,3,3,3],[4,4,4,4,4,4,4],[5,5,5,5,5,5,5],[6,6,6,6,6,6,6],[7,7,7,7,7,7,7]]
        input = np.asarray(input,dtype='float64')
        input=input.reshape((1,1,ylen,xlen))
        #print input.shape
        c = getGradXY(input)
        #print c.shape
        #这里得到的c[0]是x方向的导数，c[1]是y方向的导数
        c = c.reshape((c.shape[1],c.shape[2],c.shape[3]))
        #plt.imshow(c[1])
        return (c[0],c[1])
    #输入两块相同大小并且有略微变形的patch，计算变形程度(U,V)
    def getUV(self,img_in,img_out):
        print( img_in.dtype,img_in.shape)

        xlen = img_in.shape[1]
        ylen = img_in.shape[0]

        img_out# = img_out.reshape((1, 1, ylen, xlen))
        img_in #= img_in.reshape((1, 1, ylen, xlen))

        src_in = T.dmatrix()
        dst_in = T.dmatrix()

        src_in = src_in - T.sum(src_in)/(xlen*ylen)
        dst_in = dst_in - T.sum(dst_in)/(xlen*ylen)

        src = src_in.reshape((1, 1, ylen, xlen))
        dst = dst_in.reshape((1, 1, ylen, xlen))

        #声明两个方向平移域
        u = theano.shared(
                value=np.zeros([1, 1, ylen, xlen],dtype=theano.config.floatX),
                borrow=True
            )
        v = theano.shared(
                value=np.zeros([1, 1, ylen, xlen],dtype=theano.config.floatX),
                borrow=True
            )
        print u"声明结束"

        filter_shape = np.asarray([2,1,2,2],dtype='int')
        image_shape = np.asarray([1,1,ylen,xlen],dtype='int') #就是实际图像的大小

        #计算两个方向的梯度
        Wx=np.asarray([[-1,1],[0,0]],dtype='float64') #结果是W+Wx
        Wy=np.asarray([[-1,0],[1,0]],dtype='float64') #
        W=np.zeros(filter_shape)
        W[0,0]=Wx
        W[1,0]=Wy
        print W.shape
        #print filter_shape.shape
        #print image_shape.shape
        #首先需要计算梯度
        src_grad = conv.conv2d(
                input=src,
                filters=W,
                filter_shape=filter_shape,
                image_shape=image_shape,
                border_mode="full"
            )#卷积会忽略边界

        print u"梯度计算结束"

        #--v*src_grad[1,2,:,:])**2
        ''' '''
        gu = conv.conv2d(
                input=src,
                filters=W,
                filter_shape=filter_shape,
                image_shape=image_shape
            )#卷积会忽略边界
        gv = conv.conv2d(
                input=src,
                filters=W,
                filter_shape=filter_shape,
                image_shape=image_shape
            )#卷积会忽略边界

        cost = T.sum((dst - src+u*src_grad[0,1,0:ylen,0:xlen]+v*src_grad[0,0,0:ylen,0:xlen])**2)+0.1*T.mean(gv**2+gu**2)#+0.05*T.mean(v**2+u**2)
        params = [u,v]
        grads = T.grad(cost, params)#所有的梯度
        updates = [
            (param_i, param_i - 0.5 * grad_i)
            for param_i, grad_i in zip(params, grads)
        ]

        print u"create"
        train_model = theano.function(
            [src_in,dst_in],
            [cost,src_grad],
            updates=updates,
        )

        #theano.printing.pydotprint(train_model, outfile="tree.png", var_with_name_simple=True)
        print u"compute"
        g=[]
        a = time.time()

        for i in xrange(100):
            [c,g] = train_model(img_in,img_out)
            print c
        b = time.time()
        print b-a

        '''
        p = theano.function([src_in],src_grad)
        c = p(img_in)

        print c.dtype,c.shape
        '''
        img_in=img_in.reshape((1, 1, ylen, xlen))
        img_in=img_in[0,0,0:ylen,0:xlen]
        cp=img_in-u.get_value()*g[0,1,0:ylen,0:xlen]-v.get_value()*g[0,0,0:ylen,0:xlen]
        return (u.get_value(),v.get_value(),cp)

dp = deformed_patch()
'''
img = io.imread("F:\\tec_learn\\pythonGUI-learn\\res\\2.jpg")

#plt.imshow(img)
i = img[:,:,1]
print i.shape
(gx,gy) = dp.getXYGrad(i)

plt.imshow(gy,cmap=cm.gray)
plt.show()
'''
img_in = io.imread("F:\\tec_learn\\pythonGUI-learn\\res\\c1.jpg")
img_out = io.imread("F:\\tec_learn\\pythonGUI-learn\\res\\c2.jpg")

(u,v,cp) = dp.getUV(skimage.img_as_float(img_in[:,:,1]),skimage.img_as_float(img_out[:,:,1]))
print (u.dtype,u.shape)
u=u.reshape(u.shape[2],u.shape[3])
v=v.reshape(v.shape[2],v.shape[3])
cp=cp.reshape(cp.shape[2],cp.shape[3])
plt.subplot(2,3,1)
plt.title(u"x方向位移幅度")
plt.imshow(v,cmap=cm.gray)
plt.subplot(2,3,4)
plt.title(u"y方向位移幅度")
plt.imshow(u,cmap=cm.gray)
plt.subplot(2,3,2)
plt.title(u"输入")
plt.imshow(skimage.img_as_float(img_in[:,:,1]),cmap=cm.gray)
plt.subplot(2,3,3)
plt.title(u"变形目标")
plt.imshow(cp,cmap=cm.gray)
plt.subplot(2,3,6)
plt.title(u"变形结果")
plt.imshow(skimage.img_as_float(img_out[:,:,1]),cmap=cm.gray)
plt.show()
cp = np.asarray(cp,dtype='float64')
print cp
print skimage.img_as_float(img_out[:,:,1])