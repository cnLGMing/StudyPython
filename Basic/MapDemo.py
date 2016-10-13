# -*- coding: utf-8 -*-


# map(函数, 列表)

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

# 方法1：定义函数
def normalize(name):
    # capitalize() 是Python内置函数，意思是将首字母转为大写，其他转为小写
    return name.capitalize()

# 方法2：定义函数


def alterName(name):
    # 自定义：获取首字母并将其转为大写，其他字母转为小写
    return name[0].upper() + name[1:].lower()


L1 = ['adAm', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
L3 = list(map(alterName, L1))
print(L3)
