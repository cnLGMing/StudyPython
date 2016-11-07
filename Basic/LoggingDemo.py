#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习 Logging 的使用
# 捕获异常信息

import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) ** 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('运行结束')
