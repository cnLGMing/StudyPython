#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 学习汉诺塔，使用递归实现

def hannuota(n, x, y, z):
    if n == 1:
        print(x, '  --->  ', z)
    else:
        hannuota(n - 1, x, z, y)  # 将前 n-1 个盘子从 x 移动到 y
        print(x, '  --->  ', z)  # 将 x 最低下的盘子移动到 z
        hannuota(n - 1, y, x, z)  # 将 y 上 n-1 个盘子移动到 z


hannuota(3, 'x', 'y', 'z')
