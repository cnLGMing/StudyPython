#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习 IO 操作中读取
# 读取文件的三种方式：
#       1.一次性读取，用于少量数据
#       2.一行一行读取
#       3.一次规定读取多少字节


def readFileByAll(fileName):  # 一次行读取全部
    with open(fileName, 'r') as file:
        print(file.read())


def readFileByLine(fileName):  # 一行一行读取
    with open(fileName, 'r') as file:
        for line in file.readlines():
            print(line.strip())  # strip()去掉行首和行尾的空格


def readFileByByte(fileName, chunkCount=8):  # 规定每次读取多少 Byte
    with open(fileName, 'r') as file:
        while True:
            chunk = file.read(chunkCount)
            if not chunk:
                break
            print(chunk)


readFileByAll('Exception.txt')
print('-------------------------------')
readFileByLine('Exception.txt')
print('-------------------------------')
readFileByByte('Exception.txt', 4)
