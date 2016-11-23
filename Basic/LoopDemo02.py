#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习多线程

import time, threading


def myLoop():
    print('\t %s 正在运行!!!' % (threading.current_thread().name))
    for num in range(5):
        print('\t %s 打印了：%s' % (threading.current_thread().name, num))
        time.sleep(2)
    print('\t %s 停止运行!!!' % (threading.current_thread().name))


print('%s 开始运行' % (threading.current_thread().name))  # 获取当前线程的名称

# 创建另一个线程，并设置名称（如果没有取名字，Python 自动给我取名字 Thread-1、Thread-2...）
t = threading.Thread(target=myLoop, name='myLoop')
t.start()  # 线程开始运行
t.join()  # 另一个线程加入
print('%s 停止运行' % (threading.current_thread().name))
