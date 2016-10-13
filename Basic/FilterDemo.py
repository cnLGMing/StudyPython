# _*_ coding: utf-8 _*_

# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()滤掉非回数：

# 思路：
# 	1.将数字反转
# 	2.与原数字进行比较


def is_palindrome(n):
    return int(str(n)[::-1]) == n		# str(n)[::-1] --> 反转


print(list(filter(is_palindrome, range(1, 1000))))		# 输出 1-1000中的回数
