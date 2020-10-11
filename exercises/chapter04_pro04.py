# coding: utf-8
'''
判断用户输入的数字是偶数还是奇数

'''

while True:
    num = input("Please enter a integer('q':exit this program):")
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            print('你输入的{}是偶数。'.format(num))
        else:
            print('你输入的{}是奇数。'.format(num))
        continue
    elif num == 'q':
        break
    else:
        print('请输入整数！')