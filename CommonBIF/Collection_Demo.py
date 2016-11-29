#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习常用的内置函数之 collection

from collections import namedtuple
from collections import deque
from collections import defaultdict
from collections import OrderedDict
from collections import Counter


# namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
def namedtupleDmeo():
    Point = namedtuple('Point', ['x', 'y'])
    p = Point(1, 2)
    print('p.x = %s, p.y= %s ' % (p.x, p.y))
    Circle = namedtuple('Circle', ['x', 'y', 'r'])
    c = Circle(1, 2, 10)
    print('c.x = %s, c.y= %s, c.r = %s ' % (c.x, c.y, c.r))


# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，
# 数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
def dequeDemo():
    q = deque(['a', 'b', 'c', 'd', 'f'])
    print('源数据：', q)
    q.append('append')
    q.appendleft('appendleft')
    print('前后各插入一个数据后：', q)
    q.pop()
    q.popleft()
    print('弹出前后各一个数据后：', q)


# 使用dict时，如果引用的Key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict.
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。
# 除了在Key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
def defaultdictDemo():
    d = defaultdict(lambda: '默认值')
    d['key1'] = 'value1'
    print('key1 = %s' % d['key1'])
    print('key2 = %s' % d['key2'])


def OrderedDictDemo():
    d = dict([('a', 1), ('b', 2), ('c', 3)])
    print('dict 类型：', d)  # 无序
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print('OrderedDict 类型：', od)  # 按照插入的顺序。【不是 key 的顺序哦


def CounterDemo():
    c = Counter()
    for ch in 'Liu Guangming':
        c[ch] = c[ch] + 1
    print(c)


dequeDemo()
namedtupleDmeo()
defaultdictDemo()
OrderedDictDemo()
CounterDemo()