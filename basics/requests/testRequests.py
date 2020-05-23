#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author:james
@licence: BSD
@file: testRequests.py 
@time: 2020/05/17
@contact: lost.Fox2012+py@gmail.com
@site:  
@software: PyCharm 

"""
import requests
from bs4 import BeautifulSoup
# 从bs4这个库中导入BeautifulSoup

# link = "https://v.taobao.com/v/content/live?catetype=704" # 定义link为目标网页地址
link = 'https://v.taobao.com/v/home/?userId=1809645650&pvid=0b9226fd-7503-4c94-8894-4c7c18aabcd4&scm=1007.18171.131791.000000000000100'
# 定义请求头的浏览器代理,伪装成浏览器
headers = {'User-Agent' : 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
r = requests.get(link, headers= headers) # 请求网页
print(r.text) #r.text 是获取的网页内容代码
# soup = BeautifulSoup(r.text, "html.parser") #使用BeautifulSoup解析
# # 找到第一篇文章标题,定位到class 是"post-title" 的h1 元素,提取 a,提取a里面的字符串,strip() 去除左右空格
# title = soup.find("h1", class_="post-title").a.text.strip()
# print(title)
