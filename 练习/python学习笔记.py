#coding=gbk-----��ģ�����������ַ�����Ҫ���ע�ͣ�˵���ַ�
filename = 'learning_python.txt'
print('--' * 80)
print("��ȡ�����ļ���")
with open(filename) as file_object:
    lines = file_object.read()
    print( lines.replace('Python','C'))
print('--' * 80)
print("�����ļ�����")
with open(filename) as file_object:
    print("����հ�ԭ���ǣ��ı��ļ�ÿ���Դ��������Ļ��з�,print����Ҳ�л��й��ܣ����д����������з�")
    for line in file_object:
        print(line.replace('Python', 'C'))
with open(filename) as file_object:
    print("�������հ׷�����rstrip()-->��ĩβ�հ�ɾ����strip()-->���пհ�ɾ��")
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())
print('--' * 80)
print("�洢��һ���б���,�����б���ÿһ�У�")
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.replace('Python', 'C').rstrip())
print('--' * 80)
