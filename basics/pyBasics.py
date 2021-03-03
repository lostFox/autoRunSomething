# -*- coding: utf-8 -*-
#import PIL

#print('hello, world!')
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

# spam(0)
def collatz(num):
    if(num == 1):
        return True
    elif (num % 2 == 0):
        num /= 2
    else:
        num = num*3+1
    return collatz(num)

# print(collatz(3))
# for i in range(1, 10000):
    # if(collatz(i) == True):
        # print(i, collatz(i))

x = [1, 2, 3, "abc"]
print(type(x))
print(x[-1])

for i in range(6):
    print(i)

def getColors():
    #find /usr/local/Cellar/python/3.7.1/ -name "rgb*"
    # rgb_path = '/usr/local/Cellar/python/3.7.1//Frameworks/Python.framework/Versions/3.7/share/doc/python3.7/examples/Tools/pynche/X/rgb.txt'
    rgb_path = './rgb.txt'
    colors = []
    with open(rgb_path, ) as file:  # 打开文件
        for line in file:  # 每次读取一行
            if not (line.isspace() or line.startswith("!")):  # 空行或!打头的行则不必处理
                # 最后一个制表符之后的字符串 split("\t")[-1]
                # 再去掉末尾的换行符 [:-1] 就是颜色名
                # 把颜色名添加进列表即可
                colors.append(line.split("\t")[-1][:-1])
        print(len(colors))
        for i in colors[:]:  # 推荐这样返回一个新列表用来迭代，否则原列表改变会影响循环次数
            if " " in i or "grey" in i.lower():
                colors.remove(i)
        print(colors)
        print(len(colors))
        return colors

import turtle as tt


def showcolor(x, y, color="black"):
    """显示颜色块和颜色名
    """
    t = tt.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color(color)
    t.penup()
    t.setpos(x, y)
    t.begin_fill()
    for _ in range(4):
        t.forward(16)
        t.left(90)
    t.forward(18)
    t.end_fill()
    t.color("black")
    t.write(color)


def showcolors():
    """显示所有颜色
    """
    # from colorslist import COLORS
    COLORS = getColors()
    tt.TurtleScreen._RUNNING = True
    tt.setup(1200, 820)
    tt.setworldcoordinates(0, -810, 1200, 10)
    tt.hideturtle()
    tt.speed(0)
    tt.tracer(0)  # 关闭动效以减少耗时
    tt.penup()
    row = 0
    col = 0
    for color in COLORS:
        showcolor(col * 100, row * -18, color)
        row += 1
        if row > 45:
            row = 0
            col += 1
    tt.done()


if __name__ == "__main__":
    showcolors()

