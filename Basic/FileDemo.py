#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习基本的文件操作

file  = open('../README.md')    # 读取文件
for con in file:                # 将文件高效率的打印出来
    print(con)