#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'进行图形化界面输入，及获取输入值'

__author__ = 'cnLGMing'
__Blog__ = 'http://www.liuguangmingcn.com'
__GitHub__ = 'https://github.com/cnLGMing'

from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        # 当Button被点击时，触发self.quit()使程序退出
        self.alterButton = Button(self, text='问好', command=self.inputName)
        self.alterButton.pack()

    def inputName(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', '你好，%s' % name)


# 实例化
app = Application()
# 设置窗口的标题
app.master.title('窗口的标题')
# 主消息循环
app.mainloop()
