#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 查找文件

import os


class SearchFile(object):
    def __init__(self, fileName):
        self.__fileName = fileName

    def __chekName(self, fileName, searchDir):
        if self.__fileName in fileName:  # 判断文件名是否包含了需要查找的内容字符
            print('文件名：%s, -----> 其绝对路径为：%s' % (fileName, os.path.join(searchDir, fileName)))

    def startSearchFile(self, searchDir="."):
        for x in os.listdir(searchDir):
            if os.path.isdir((os.path.join(searchDir, x))):  # 判断当前是否为文件夹
                # 若是文件夹，则进入文件夹内，递归
                self.startSearchFile((os.path.join(searchDir, x)))
            elif os.path.isfile((os.path.join(searchDir, x))):  # 判断当前是否为文件
                # 若是文件，则进行判断其文件名中是否包含了需要查找的内容字符
                self.__chekName(x, searchDir)


fileName = input('请输入，你需要查找的文件名所包含的内容：')
searchFile = SearchFile(fileName)
searchFile.startSearchFile('/Users/LGMing/Python_Projects')
print('扫描结束！')
