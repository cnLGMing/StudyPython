# _*_ coding: utf-8 _*_

# 使用列表生成器，列出指定路径下的文件名和文件夹名
import os

print([ d for d in os.listdir('.') ])