#coding=gbk
filename = 'pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = ""
while birthday != 'quit':
    birthday = input("�������������գ�")
    if birthday == 'quit':
        break
    elif birthday in pi_string:
        print("������������1000000Բ����ֵ�У�")
    else:
        print("������ղ���Բ����ֵ�У�����")
