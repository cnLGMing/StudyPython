#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading

local_school = threading.local()  # 创建全局ThreadLocal 对象


def printStuInfo():
    stu = local_school.student  # 获取当前线程所关联的 Student
    print('你好，%s 的 %s' % (threading.current_thread().name, stu))


def threadStu(name):
    local_school.student = name  # 绑定ThreadLocal的 Student
    printStuInfo()


t1 = threading.Thread(target=threadStu, args=('小明',))
t2 = threading.Thread(target=threadStu, args=('小刘',))

t1.start()
t2.start()
t1.join()
t2.join()

# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

# 一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
