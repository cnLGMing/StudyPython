#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5
import hashlib
from collections import defaultdict

db = defaultdict(lambda: 'null')


def get_md5(param):
    md5 = hashlib.md5()
    md5.update(str(param).encode('utf-8'))
    return md5.hexdigest()


# 注册
def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
    print('注册成功')


# 登录
def login(username, password):
    pwd = get_md5(password + username + 'the-Salt')
    if db[username] == pwd:
        print('登录成功')
    else:
        print('登录失败')


hasUserName = input('是否已有账号密码? yes/no:\n')
if hasUserName == 'y':
    username = input('请输入用户名:')
    pwd = input('请输入密码:')
    login(username, pwd)
else:
    print('欢迎注册新用户')
    username = input('请输入用户名:')
    pwd = input('请输入密码:')
    register(username, pwd)
    login(username, pwd)
