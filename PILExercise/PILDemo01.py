#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

# 打开一张图片,权限:只读
image = Image.open('girl.png', mode='r')
# 获取图片的宽和高
wide, high = image.size
print('原图图片的宽: %s, 高: %s' % (wide, high))
# 缩放为原图的50%
image.thumbnail((wide // 2, high // 2))
print('原图图片的宽: %s, 高: %s' % (wide // 2, high // 2))
# 修改后的图片保存,指定格式
image.save('girl_thumbnail.jpg', 'jpeg')
