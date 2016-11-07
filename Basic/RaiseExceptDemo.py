#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 学习抛出自定义异常
# 1. 自定义异常
# 2. 使用 raise 抛出自定义异常

class MyExcept(ZeroDivisionError):
    print('有自定义异常')
    pass


def foo(s):
    num = int(s)
    if (num == 0):
        raise MemoryError('invalid value: %s' % s)
    return 10 / num


foo('0')
