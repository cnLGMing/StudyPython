#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 摘要用算法

import hashlib


# md5 算法 Demo
def md5Demo():
    md5 = hashlib.md5()
    md5.update('刘广明'.encode('utf-8'))
    print('[刘广明] 进行 MD5 加密后:%s' % md5.hexdigest())


# SHA1 算法 Demo
def SHA1Demo():
    sha1 = hashlib.sha1()
    sha1.update('刘广明'.encode('utf-8'))
    print('[刘广明] 进行 SHA1 加密后:%s' % sha1.hexdigest())


md5Demo()
SHA1Demo()
