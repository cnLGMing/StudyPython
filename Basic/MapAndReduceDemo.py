# _*_ coding:utf-8 _*_

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
# 思路：1.获取小数点的下标point
# 		2.将小数点去掉
# 		3.将'123456'转换为int
# 		4.将123456除于(10的(字符串的长度-point))次方


from functools import reduce


def fn(x, y):
    return 10 * x + y		# 计算num


def char2num(s):			# 通过 Python 的 dict返回 字符所对应的 数字value
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2float(s):
    point = s.find('.') 		# 获取小数点的下标
    s = s.replace('.', '')		# 将小数点干掉
    # 计算最终值
    return (reduce(lambda x, y: x * 10 + y,
                   map(char2num, s))) / (10 ** (len(s) - point))


print('str2float(\'123.456\') =', str2float('123.456'))
