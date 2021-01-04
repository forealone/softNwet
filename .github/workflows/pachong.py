# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 08:55:48 2020

@author: User
"""

from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as bf

#请求获取html
html = urlopen("http://www.baidu.com/")
#获取的html内容是字节，将其转化为字符串
html_text = bytes.decode(html.read())
print(html_text)


#用bf解析html
obj = bf(html.read(),'html.parser')
#从标签head、title里提取标题
title = obj.head.title
print(title)

#使用find_all函数获取所有图片信息
pic_info = obj.find_all('img')
for i in pic_info:
    print(i)
    
#只提取logo图片的信息
logo_pic_info = obj.find_all('img', class_="index-logo-src")
#提取图片链接
logo_url = "https:"+logo_pic_info[0]['src']
#打印链接
print(logo_url)
#下载图片(C:\用户\user\)
urlretrieve(logo_url, 'baidu_logo.png')



html = urlopen("https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E7%BF%B1%E7%BF%94")
obj = bf(html.read(),'html.parser')
pic_info = obj.find_all('img')
logo_url = pic_info[0]['src']
urlretrieve(logo_url, 'echarts123.png')
