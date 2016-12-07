#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

image = Image.open('girl.png', mode='r')
# 模糊化
image2 = image.filter(ImageFilter.BLUR)
image2.save('girl_blur.jpg', 'jpeg')
