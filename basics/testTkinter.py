#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
@author:james
@licence: BSD
@file: testTkinter.py 
@time: 2019/01/06
@contact: lost.Fox2012+py@gmail.com
@site:  
@software: PyCharm 

"""

import tkinter as tk

def change(widget, var):
    """事件处理函数：改变Text部件的文本
    在widget现有文本末尾插入新的文本var
    """
    widget.config(state="normal")
    widget.insert("end", var + "\n")
    widget.config(state="disabled")

def main():
    window = tk.Tk()  # 生成窗口对象
    window.geometry("500x300")  # 设置窗口大小
    window.title("简单图形界面程序")  # 设置窗口标题

    # 这里可以生成其他部件并放入窗口
    label = tk.Label(window, text="请输入文本并点击添加")
    label.grid(row=0, column=0)
    entry = tk.Entry(window, width=50)
    entry.grid(row=1, column=0, columnspan=2, padx=20, pady=10)
    text = tk.Text(window, width=50, height=12, background="wheat")
    text.config(state="disabled")
    text.place(x=20, y=100)
    button = tk.Button(window, text="添加",
                       command=lambda: change(text, entry.get()))
    button.grid(row=0, column=1)

    tk.mainloop()  # 开始主循环

if __name__ == "__main__":
    main()


