#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request


# 对豆瓣的一个URL https://api.douban.com/v2/book/2129650 进行抓取，并返回响应
def catchURLGet(target_url):
    print('-----------  开始请求数据  ------------')
    with request.urlopen(target_url) as f:
        data = f.read()
    print('状态码:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s : %s' % (k, v))
    print('数据:', data.decode('utf-8'))


catchURLGet('https://api.douban.com/v2/book/2129650')
