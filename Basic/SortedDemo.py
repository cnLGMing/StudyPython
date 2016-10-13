# _*_ coding:utf-8 _*_

# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 1. 请用sorted()对上述列表分别按名字排序：
# 2. 再按成绩从高到低排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print('按照名字升序：', list(sorted(L, key=lambda L_tuple: L_tuple[0])))
print('按照成绩升序：', list(sorted(L, key=lambda L_tuple: L_tuple[1])))

print('按照名字降序：', list(sorted(L, key=lambda L_tuple: L_tuple[0], reverse=True)))
print('按照成绩降序：', list(sorted(L, key=lambda L_tuple: L_tuple[1], reverse=True)))
