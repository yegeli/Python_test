# coding=gbk
message = "���û�����������"
h = input(message)
filename = 'guest.txt'
with open(filename,'w') as object:
    object.write(h + "\n")
