#coding=gbk-----该模块中有中文字符，需要添加注释，说明字符
filename = 'learning_python.txt'
print('--' * 80)
print("读取整个文件：")
with open(filename) as file_object:
    lines = file_object.read()
    print( lines.replace('Python','C'))
print('--' * 80)
print("遍历文件对象：")
with open(filename) as file_object:
    print("多余空白原因是：文本文件每行自带看不见的换行符,print函数也有换行功能，所有存在两个换行符")
    for line in file_object:
        print(line.replace('Python', 'C'))
with open(filename) as file_object:
    print("解决多余空白方法：rstrip()-->行末尾空白删除，strip()-->整行空白删除")
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())
print('--' * 80)
print("存储在一个列表中,遍历列表中每一行：")
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.replace('Python', 'C').rstrip())
print('--' * 80)
