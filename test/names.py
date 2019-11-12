#coding=gbk
from name_function import get_formatted_name
print("输入'q'立刻退出.")
while True:
    first = input("请输入姓: ")
    if first == 'q':
        break
    last = input("请输入名字: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print("全名： " + formatted_name + '.')

