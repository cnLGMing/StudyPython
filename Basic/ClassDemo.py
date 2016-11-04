#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习类


class MyTest(object):
    def __len__(self):
        return 100


test = MyTest()
print(len(test))


class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an Integer.')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 - 100')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, year):
        if not isinstance(year, int):
            raise ValueError('年份必须是整数')
        if year < 0 or year > 2016:
            raise ValueError('年份不合理的')
        self._birth = year

    @property
    def age(self):
        return 2016 - self._birth


stu = Student()
stu.score = 100
print('成绩：', stu.score)
stu.birth = 1993
print('年龄：', stu.age)


