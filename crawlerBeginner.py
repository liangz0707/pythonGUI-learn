
# coding: utf-8

# #网页爬虫、request、BS4学习

# #1.request使用

# ##1.1获取get请求

# In[8]:

import requests 


# In[10]:

#无参数get请求
req = requests.get('http://httpbin.org/get')
page = req.text #获取页面文本
#带参数get请求
params = {'q':'杨彦星'}
req = requests.get('http://httpbin.org/get', params = params)
req.url #得到请求的url


# ##1.2获取post请求

# In[15]:

#含参post请求
params = {'a':'杨','b':'hello'}
req = requests.post('http://httpbin.org/gpost',data = params)
page = req.text #获取页面信息
#提交json格式请求
params = {'a':'杨','b':'hello'}
import json
req = requests.post('http://httpbin.org/post', data=json.dumps(params))


# ##1.3提交文件

# In[17]:

#提交文件 需要files参数
url = 'http://httpbin.org/post'
files = {'file': open('1.jpg', 'rb')}
req = requests.post(url, files=files)


# ##1.4使用header提交文件

# In[25]:

import json
url = 'https://www.baidu.com'
params = {'some': 'data'}
headers = {'content-type': 'application/json'}
req = requests.post(url, data=json.dumps(params), headers=headers)


# ##1.5响应操作

# In[29]:

print req.headers
print req.headers['Content-Type']
print req.status_code


# #2.BeautifulSoup

# In[34]:

#测试文档
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


# In[36]:

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())


# In[74]:

#只能获取到第一个标签
soup.title
#获取标签的属性
print(soup.title.name)
#获取父节点
print(soup.title.parent.name)
#获取属性
soup.p['class']


# In[39]:

#获取所有标签
for link in soup.find_all('a'):
    #获取标签下的属性
    print(link.get('href'))


# #3.request和BeautifulSoup连接

# In[40]:

req = requests.get("http://www.baidu.com")
page = req.text #获取界面文本
soup = BeautifulSoup(page,"html.parser")


# #4.网页爬取

# In[ ]:

#同上


# #5.图片爬取

# In[53]:

import os
def saveImage( imgUrl,imgName ="default.jpg" ):
    response = requests.get(imgUrl, stream=True)
    image = response.content
    DstDir=os.getcwd() #保存在当前工作目录下
    print("保存文件"+imgName+"\n")
    try:
        with open(os.path.join(os.getcwd(),'image',imgName) ,"wb") as jpg:
            jpg.write( image)     
            return
    except IOError:
        print("IO Error\n")
        return
    finally:
        jpg.close        


# In[55]:

#生成时间戳保证下载的内容文件名不重复
import time
def getT():
    t = time.time()
    s = str(int(t*100%10000000))
    return s


# #6.爬取百度贴吧图片

# In[71]:

#首先需要请求一个贴吧的主页
main_url = "http://tieba.baidu.com/f"
page_num = 2 #用与计算需要爬取的页数
title_list= [] #保存所有要爬取帖子的链接
for i in range(page_num): 
    params = {"kw" : "python" , "pn":i*50} #通过页码和关键字决定
    req = requests.get(main_url,params=params) #得到一个页面
    page = req.text #得到页面文本
    soup = BeautifulSoup(page,'html.parser')
    a_list = soup.find_all("a")
    hrefs = [t.get("href") for t in a_list if t.get("class") and t.get("class")[0]=="j_th_tit"]
    title_list.extend(hrefs)
#print(title_list)


# In[72]:

#进行url拼装
import urlparse
#url拼接的例子
print urlparse.urljoin('http://somehost.com/', '../other/path')
#进行拼接
title_list = [urlparse.urljoin( main_url , t) for t in title_list]
#print title_list


# In[80]:

title_list = title_list[0:5]#节省时间 ，暂时先用前几个帖子
image_url_list = [] #保存所有获取到图片的url 供之后下载
for t_url in title_list: #处理每一个主题页面
    pn_num = 1 #先假设只有一页
    i=0
    while i< pn_num :
        i = i+1
        #设置页面参数
        param = {"see_lz" : 1 ,"pn":i+1}  #只抓取楼主的内容
        req = requests.get(t_url,param)
        page = req.text
        soup = BeautifulSoup(page,'html.parser')
        im_list = soup.find_all("img") #先获取图片元素
        im_list = [t.get("src") for t in im_list if t.get("class") and t.get("class")[0]=="BDE_Image"]
        image_url_list.extend(im_list)
        
        #获取真实的页数
        pnc = soup.find_all("span")
        pnc = [p.text for p in pnc if p.get("class")and p.get("class")[0] == "red"]
        pn_num =  int(pnc[1]) 
        
print(image_url_list)


# In[82]:

#开始下载
for img_url in image_url_list :
    saveImage(img_url , getT()+".jpg")

# In[ ]:



