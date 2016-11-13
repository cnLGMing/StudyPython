#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('操作系统的名称：', os.name)
print('获取系统的详细信息：\n', os.uname())  # 此函数在 Windows 下无效
print('当前路径：', os.path.abspath('.'))

# 创建文件夹
# join函数可以正确处理不同系统的路径分隔符
# os.mkdir(os.path.join('/Users/LGMing/Python_Projects/StudyPython/Basic', 'mkdirFile'))

# 删除文件夹
# os.rmdir(os.path.join('/Users/LGMing/Python_Projects/StudyPython/Basic', 'mkdirFile'))


# 获取文件的后缀名
print('文件的后缀名：', os.path.splitext('/Users/LGMing/Python_Projects/StudyPython/Basic/FielDemo.py')[1])

# 创建一个不存在的文件，并进行重命名
with open('./Demo.txt', 'w') as file:
    os.rename('Demo.txt', 'renameFileDemo.txt')  # 对文件进行重命名
    print('文件名修改成功！')

# 删除文件
os.remove('./renameFileDemo.txt')
print('文件删除成功！')
