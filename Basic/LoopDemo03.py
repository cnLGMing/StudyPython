#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习多线程 加锁前奏

import threading, time

money = 0


def change_money(n):
    # 模仿先存钱后取钱的操作，按道理来说，应该为0
    global money
    money = money + n
    money = money - n


def run_thread(n):
    for i in range(1000000):  # 需要循环足够的次数，才会出现问题
        change_money(n)


print('我现在有 %s 元。马上我就要去银行存钱取钱了。' % (money))
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('我还有 %s 元' % (money))
