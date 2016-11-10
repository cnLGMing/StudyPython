#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 学习 IO 操作中的写入操作

def wirteFile(filePath):
    with open(filePath, 'w', encoding='utf-8') as file:
        file.write('学习 IO 操作中的写入操作')


wirteFile('./StudyWriteFile.txt')
print('写入完毕')
