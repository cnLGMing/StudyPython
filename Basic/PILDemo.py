#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' 学习如何导入并使用第三方模块 '

# 需要先添加第三方模块：Pillow

__author__ = 'cnLGMing'

from PIL import Image

im = Image.open('/Users/LGMing/Pictures/picture.jpg')
print(im.format, im.size, im.mode)
im.thumbnail((150, 220))
im.save('/Users/LGMing/Pictures/copy_picture.jpg', 'JPEG')
