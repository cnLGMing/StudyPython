#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
def readFileEnoding(fileName):
    with open(fileName, 'r', encoding='gbk') as file:  # encoding 是指定编码
        print(file)


# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
# 最简单的方式是直接忽略：
def readFileEnodingAndError(fileName):
    with open(fileName, 'r', encoding='gbk', errors='ignore') as file:
        print(file)
