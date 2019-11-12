# coding=gbk
message = "请用户输入姓名："
h = input(message)
filename = 'guest.txt'
with open(filename,'w') as object:
    object.write(h + "\n")
