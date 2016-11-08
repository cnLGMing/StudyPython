#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 常见的 raise 使用方式

def division(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError('divisor 是除数，在除法运算中，除数不能为 0')
    return dividend / divisor


def main():
    try:
        division(10,0)
    except ZeroDivisionError as e:
        print('出现异常:', e)
        raise


main()
