# coding: utf-8
'''
编写一个程序，能够输出字符串“Hello”中每个“l”的索引值。
'''

s = 'hello'
n = s.count('l')  # l的个数，循环次数
index_lst = []  # 先创建索引值的空列表
start = 0  # index方法的start值

for i in range(n):
    idx = s.index('l', start)
    start = idx + 1  # 下一次索引时从上次得到的索引值开始
    index_lst.append(idx)  # 索引值添加进索引值列表

print(index_lst)