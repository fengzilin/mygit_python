# coding: utf-8
'''
寻找能够被17整除的三位正整数。

'''
# d = []
# for n in range(100, 1000):
#    if n % 17 == 0:
#        d.append(n)
#    else:
#        continue
# print(d)
# 列表解析只需要一条语句
lst = [n for n in range(100, 1000) if n % 17 == 0]
print(lst)