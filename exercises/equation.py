# coding: utf-8
'''
    求解一元二次方程
'''
import math

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

delta = b * b - 4 * a * c

if delta > 0:
    sqrt_delta = math.sqrt(delta)
    root1 = (-b + sqrt_delta) / (2 * a)
    root2 = (-b - sqrt_delta) / (2 * a)
    print('The root is: {0} and {1}'.format(root1, root2))
elif delta == 0:
    root = -b / (2 * a)
    print('The root is: {0}'.format(root))
else:
    print('no root')