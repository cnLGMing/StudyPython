#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request, parse

print('准备登陆 ---> 新浪微博')
username = input('请输入用户名:')
password = input('请输入密码:')
login_data = parse.urlencode([  #
    ('username', username),  #
    ('password', password),  #
    ('entry', 'mweibo'),  #
    ('client_id', ''),  #
    ('savestate', '1'),  #
    ('ec', ''),  #
    ('pagerefer',  #
     'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

print('正在登陆...')
with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('状态码: ', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s : %s' % (k, v))
    print('数据: ', f.read().decode('utf-8'))
