#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author:james
@licence: BSD
@file: testSelenium.py 
@time: 2020/05/17
@contact: lost.Fox2012+py@gmail.com
@site:  
@software: PyCharm 

"""
from selenium import webdriver
driver = webdriver.Chrome('/home/james/bin/chromedriver')
driver.get('https://v.taobao.com/v/content/live?catetype=704')

comment = driver.find_element_by_css_selector('ice-img sharp anchor-avatar')
#content = comment.find_element_by_tag_name('img')
#print(content)
