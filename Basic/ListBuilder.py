# -*- coding: utf-8 -*-

# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
# ['Hello', 'World', 18, 'Apple', None]
# 期待输出 ['hello', 'world', 'apple', None]

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])