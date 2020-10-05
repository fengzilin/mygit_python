# coding: utf-8
'''
有列表 lst=［'anwang'，'microsoft'，'ibm'，'compaq'，'lenovo'，'dell'］，
请将列表中含有字母 a 的字符串挑选出来,追加到一个列表中。
'''

lst = ['anwang', 'microsoft', 'ibm', 'compaq', 'lenovo', 'dell']
new_lst = []  # 先创建一个空列表

for l in lst:
    if 'a' in l:
        new_lst.append(l)

print(new_lst)