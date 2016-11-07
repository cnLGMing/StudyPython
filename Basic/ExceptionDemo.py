#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习异常、捕获异常

# 加入现在创建一个文件，并写入数据，但在还没来得及关闭文件时，产生了一个异常

# 跟 Java 相似


try:
    create_file = open('Exception.txt', 'w')
    create_file.writelines('我是为了演示异常而新建的文件')
    sum = 1 + '1'
except OSError as reason:  # 进行捕获异常、reason 是指具体的异常信息
    print('出现异常，异常是：' + reason)
except TypeError as reason:
    print('出现异常，异常是：' + reason)
finally:
    create_file.writelines('\n 这行是在 finally添加的。')
    create_file.close()
    print('程序结束')
