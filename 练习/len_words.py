# coding=gbk
filename = 'alice.txt'

try:
    with open(filename,encoding = 'UTF-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    # �����ļ����°������ٸ�����
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")