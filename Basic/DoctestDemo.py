#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习文档测试


def fact(n):
    '''
    Funcation to get value of Recursion

    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6

    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
