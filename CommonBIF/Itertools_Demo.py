#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习内置函数 itertools
import itertools


def countDemo():
    cou = itertools.count(1)  # 这是一个无限迭代器
    for num in cou:
        print(num)


def count2Demo():
    cou2 = itertools.count(1)  # 通过takewhile()等函数根据条件判断来截取出一个有限的序列
    lists = itertools.takewhile(lambda x: x <= 10, cou2)
    print(list(lists))


def cycleDemo():  # 重复循环打印 a b c a b c a b c
    cy = itertools.cycle('abc')
    for x in cy:
        print(x)


def repeatDemo():  # 迭代指定次数\指定系列 abc abc abc
    re = itertools.repeat('abc', 3)
    for r in re:
        print(r)


def chainDemo():  # 把一组迭代对象串联起来，形成一个更大的迭代器
    for c in itertools.chain('abc', 'xyz'):
        print(c)


def groupbyDemo():  # 把迭代器中相邻的重复元素挑出来放在一起：
    for key, value in itertools.groupby('aabbbcddeeeae'):
        print(key, list(value))


# countDemo()
# count2Demo()
# cycleDemo()
# repeatDemo()
# chainDemo()
groupbyDemo()
