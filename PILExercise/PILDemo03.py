#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random

# 用于记录生成的字母
resultChar = ""


# 生成字母随机码
# 随机字母
def randomChar():
    while (True):
        num = random.randint(48, 122)
        if (not ((57 < num < 65) or (90 < num < 97))):  # 排除不合法数据
            break;
    return chr(num)  # 数字:48-57; 大写字母:65-90; 小写字母:97-122


# 随机颜色1
def randomColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def randomColor2():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 整个背景的大小,并创建白色背景
width = 60 * 4
high = 80
image = Image.new('RGB', (width, high), (255, 255, 255))

# 创建字体对象
font = ImageFont.truetype('Arial.ttf', 60)

# 创建Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素的颜色
for x in range(width):
    for y in range(high):
        draw.point((x, y), fill=randomColor1())

# 输出字母
for t in range(4):
    draw.text((60 * t + 10, 10), randomChar(), fill=randomColor2(), font=font)

image = image.filter(ImageFilter.BLUR)
isSave = image.save('验证码.jpg', 'jpeg')
print('验证码: ---> 保存成功!')
