# coding:utf-8
'''
    -计算圆的周长和面积
    -提示用户输入半径（23）
'''
import math

radius = float(input("Enter the radius of circle: "))  // 参考老师的答案做了修改
circumference = math.pi * radius * 2
area = math.pi * radius * radius

print('The circumference is :', round(circumference, 2))
print('The area is :', round(area, 2))
