#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 请利用@property 给一个 Screen 对象加上 width 和 height 属性，
# 以及一个只读属性 resolution:

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError('屏幕的宽度不合理')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError('屏幕的高度不合理')
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)

assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

print("测试成功")



