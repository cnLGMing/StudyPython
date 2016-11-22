#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习多线程

import os

# 获取当前的线程 id
print('当前的线程id = %s ' % (os.getpid()))

pid = os.fork()  # 此方法只能在 Unix、Linux使用，Windows 不能调用此方法

if pid == 0:
    print('我是子线程，我的 id 是：%s；我是由 %s 创建的。' % (os.getpid(), os.getppid()))
else:
    print('我【%s】创建了一个子线程，id 为 %s ' % (os.getpid(), pid))

