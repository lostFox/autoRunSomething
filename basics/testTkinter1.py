"""tkimage.pyw 简单的图片查看器
"""
import tkinter as tk
import tkinter.filedialog as fd


def openimage(canvas):
    """事件处理函数：使用文件对话框打开图片
    """
    filename = fd.askopenfilename(filetypes=[("PNG图片", "*.png"),
                                             ("GIF图片", "*.gif")])
    global image  # 注意这个需要定义为全局变量
    image = tk.PhotoImage(file=filename)
    canvas.create_image((0, 0), image=image, anchor="nw")


def main():
    """主函数：设置窗口部件，指定按钮点击事件处理函数
    """
    window = tk.Tk()
    window.geometry("600x480")
    window.title("简单的图片查看器")
    canvas = tk.Canvas(window, width=600, height=440)
    canvas.pack(side="bottom")
    button = tk.Button(window, text="打开图片",
                       command=lambda: openimage(canvas))
    button.pack()
    tk.mainloop()


if __name__ == "__main__":
    main()
