#coding=gbk
from name_function import get_formatted_name
print("����'q'�����˳�.")
while True:
    first = input("��������: ")
    if first == 'q':
        break
    last = input("����������: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first,last)
    print("ȫ���� " + formatted_name + '.')

