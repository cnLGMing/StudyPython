#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习 logging 打印日志消息

import logging

logging.basicConfig(level=logging.INFO)


def main(s):
    n = int(s)
    logging.info('10 / %d =  %d' % (n, 10 / n))
    print('10 / %d =  %d' % (n, 10 / n))


main(10)
