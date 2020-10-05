# coding: utf-8
'''
请判断用户的键盘输入，如果输入的都是数字，则把该数字扩大10倍，再打印结果；
如果输入的是字符a ～ z，在其后面增加“@ python”，再打印结果；
其他情况则直接打印出来。
'''

input_char = input('Input something: ')
if input_char.isdigit():
    result = int(input_char) * 10
    print('You input {0}. Output {1}.'.format(input_char, result))
elif input_char.isalpha():
    result_str = input_char + '@ python'
    print('You input {0}. Output {1}.'.format(input_char, result_str))
else:
    print('You input:', input_char)