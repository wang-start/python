'''
制作一个满足如下功能的猜数游戏：
计算机随机生成一个100以内的正整数；
用户通过键盘输入数字，猜测计算机所生成的随机数。
注意：对用户的输入次数不做限制。
'''
import random
import sys
n = random.randint(0,100)

while True: 
    user_1 = input("请输入你猜的数：")
    if user_1 == 'esc':
        print('好的 马上结束')
        sys.exit()
    elif not user_1.isdigit():   #isdigit()方法判断字符串内是不是整数
        print('输入不正确 请输入数字')
        continue
    user = int(user_1)
    if n < user:
        print("不对额 your number is big 请重新输入！")
    elif n > user:
        print("不对额 your number is small 请重新输入！")
    else:
        print("恭喜你猜对了！")
        break

        
