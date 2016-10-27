#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 学习对象。有 Java 知识，感觉学起来还是蛮简单的。




class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printInfo(self):
        print('学生信息：\n\t姓名：%s , 年龄：%s' % (self.name, self.age))


stu = Student('刘广明', 23)
stu2 = Student('lgm', 22)
stu.printInfo()
stu2.printInfo()
