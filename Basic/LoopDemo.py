# _*_  coding: utf-8 _*_
# 请利用循环依次对list中的每个名字打印出Hello, xxx!：

L = ['小刘', '广明', '阿广']
print('---  for 循环	 ---')
for name in L:
	print('Hello, %s !' %(name))

print('---  while 循环	 ---')
i = 0
while i < len(L):
	print('Hello, %s !' %(L[i]))
	i = i + 1