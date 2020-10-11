# coding: utf-8
'''
chapter04pro3
编写程序，当用户输入某一速度值的时候，判断物体以该速度运动的结果。 
'''
while True:
    velocity = input(
        "Please input a certain speed value, \
the unit of speed is km/s.\n('q':exit this program):"
    )
    try:
        type(eval(velocity)) != float and type(eval(velocity)) != int
        # 通过eval函数和异常判断语句（try/except）判断输入是否为数字（整数和浮点数）
        velocity = float(velocity)

        if velocity < 7.9:
            print('你输入的速度{}km/s达不到宇宙速度。'.format(velocity))
        elif 7.9 <= velocity < 11.2:
            print('你输入的速度是{}km/s，物体将环绕地球运动。'.format(velocity))
        elif 11.2 <= velocity < 16.7:
            print('你输入的速度是{}km/s，物体将环绕太阳运动。'.format(velocity))
        elif 16.7 <= velocity < 22:  # 22km/s是假设值
            print('你输入的速度是{}km/s，物体将飞出太阳系。'.format(velocity))
        else:
            print('这个速度目前的技术还做不到。')
        continue
    except:
        if velocity == 'q':
            break
        else:
            print("你输入的不是数字哦。")