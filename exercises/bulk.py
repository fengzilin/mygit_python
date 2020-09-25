# conding: utf-8
'''
    计算圆柱体的体积
'''

import math

radius = int(input('Enter the radius of the cylinder: '))
high = int(input('Enter the high of the cylinder: '))
bulk = math.pi * radius * radius * high

print('The bulk of cylinder is: ', round(bulk, 2))