# _*_ coding:utf-8 _*_

# 使用生成式，列出杨辉三角

n = 0


def triangles():
    L = [1]
    while True:
        yield L
        L.append(0)
        L = [(L[i - 1] + L[i]) for i in range(len(L))]


for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
