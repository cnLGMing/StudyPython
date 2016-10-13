#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

# 	请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# 		ax2 + bx + c = 0 的两个解。
# 提示：计算平方根可以调用math.sqrt()函数：import math

import math


def quadratic(a, b, c):
    # 先判断a,b,c 是否是合法数据
    if not isinstance(a, (int, float)):
        raise TypeError('%s 数据不合法, a只限于整数与浮点数' % a)
    if not isinstance(b, (int, float)):
        raise TypeError('%s 数据不合法, b只限于整数与浮点数' % b)
    if not isinstance(c, (int, float)):
        raise TypeError('%s 数据不合法, c只限于整数与浮点数' % c)

    Delta = b**2 - (4 * a * c)
    if Delta < 0:
        print('此方程无解')
        return
    elif Delta == 0:
        x1 = -b / (2 * a)
        print('此方程有一个实根 x = %s' % x1)
        return x1
    elif Delta > 0:
        x1 = (-b + math.sqrt(Delta)) / (2 * a)
        x2 = (-b - math.sqrt(Delta)) / (2 * a)
        print('此方程有两个实根 x1 = %s，x2 = %s' % (x1, x2))
        return x1, x2


quadratic(2, 3, 1)		# 调用方法
quadratic(1, 3, -4)
quadratic(1, 2, 1)
quadratic(1, -2, 1)
quadratic('a', 3, 1)
