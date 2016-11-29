#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 请写一个能处理去掉=的base64解码函数：

# -*- coding: utf-8 -*-

import base64


def safe_base64_decode(s):
    s_len = len(s)
    needAdd = 4 - (s_len % 4)
    s = s + (b'=' * needAdd)
    print(s)
    return base64.urlsafe_b64decode(s)


assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('Pass')
