#coding=gbk
while True:
    message = '�������û�����'
    name = input(message)
    if name == 'quit':
        break
    print(name + '��ӭ����')
    filename = 'guest_book.txt'
    with open(filename,'a') as object:
        object.write(name + '\n')