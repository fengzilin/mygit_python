# coding: utf-8
'''
假设三角形三条边分别用a、b、c表示，三边所对的角为A、B、C，
那么有c^2 = a^2 + b^2 - 2ab*cos(C)。
若已知三边长度分别为3、7、9，请计算出三角形三个角（用弧度制表示）
'''
import math

a = int(input('Enter a: '))
b = int(input('Eeter b: '))
c = int(input('Enter c: '))
# c^2 = a^2+b^2-2abcosC
# a^2 = b^2+c^2-2bccosA
# b^2 = a^2+c^2-2accosB

angle_a = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
angle_b = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
angle_c = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
# angle_c = math.pi - angle_a - angle_b

print('The angle_a is: ', round(angle_a, 4))
print('The angle_b is: ', round(angle_b, 4))
print('The angle_c is: ', round(angle_c, 4))