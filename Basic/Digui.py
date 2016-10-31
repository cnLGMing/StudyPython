#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 学习递归



def digui(num):
    if num < 1:
        print('数据有误！！！')
        return -1
    if num == 1 or num == 2:
        return 1
    else:
        return digui(num - 1) + digui(num - 2)

restult = digui(20)
print('一共有多少？%d' %(restult))


