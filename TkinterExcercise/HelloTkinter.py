#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 第一个图形化界面例子


from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='第一个 Tkinter 图形化界面')
        self.helloLabel.pack()
        # 当Button被点击时，触发self.quit()使程序退出
        self.quitButton = Button(self, text='退出', command=self.quit)
        self.quitButton.pack()


# 实例化
app = Application()
# 设置窗口的标题
app.master.title('窗口的标题')
# 主消息循环
app.mainloop()


# GUI程序的主线程负责监听来自操作系统的消息，并依次处理每一条消息。
# 因此，如果消息处理非常耗时，就需要在新线程中处理。
