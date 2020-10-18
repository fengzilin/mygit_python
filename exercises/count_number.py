# coding: utf=8
'''
创建一个数据集，包含1到10的随机整数，共计100个数。并统计每个数字出现的次数。
'''

import random

lst = []
for i in range(100):
    n = random.randint(1, 10)
    lst.append(n)

d = {}
for n in lst:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1
print(d)