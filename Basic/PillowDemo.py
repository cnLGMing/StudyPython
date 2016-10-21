#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

im = Image.open('/Users/LGMing//Pictures//picture.jpg')
print(im.format, im.size, im.mode)

