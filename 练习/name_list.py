#coding=gbk
while True:
    message = '请输入用户名：'
    name = input(message)
    if name == 'quit':
        break
    print(name + '欢迎您！')
    filename = 'guest_book.txt'
    with open(filename,'a') as object:
        object.write(name + '\n')