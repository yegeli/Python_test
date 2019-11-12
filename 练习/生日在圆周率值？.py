#coding=gbk
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = ""
while birthday != 'quit':
    birthday = input("请输入您的生日：")
    if birthday == 'quit':
        break
    elif birthday in pi_string:
        print("你的生日在这个1000000圆周率值中！")
    else:
        print("你的生日不在圆周率值中！！！")
