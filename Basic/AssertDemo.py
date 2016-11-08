#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习断言 Assert 的使用方式

def main(s):
    assert isinstance(int(s), int), 'n 数据不合法'
    n = int(s)
    assert n != 0, ' n = 0'
    return 10 / n


print(main(1))
print(main('o'))
