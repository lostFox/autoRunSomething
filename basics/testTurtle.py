#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author:james
@licence: BSD
@file: testTurtle.py 
@time: 2018/11/28
@contact: lost.Fox2012+py@gmail.com
@site:  
@software: PyCharm 

"""

import turtle as tt

tt.TurtleScreen._RUNNING = True  # 启动绘图，在IDE中运行加这句可避免报错

tt.bgcolor("black")  # 背景色为黑色
tt.colormode(255)  # 颜色模式为真彩色
tt.pencolor("white")  # 画笔颜色每次随机

#cnt = 0
#while cnt < 5:
#    tt.forward(200)
#    tt.right(144)
#    cnt += 1

for i in range(0, 6):
    for j in range(0, 6):
        tt.forward(100)
        tt.right(60)
    tt.right(60)

tt.done()  # 结束绘图，这将不会关闭窗口
