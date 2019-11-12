def cat_and_dog(filename):
    try :
        with open(filename,'r') as f:
            notes = f.read()

    except FileNotFoundError:
        pass
    else:
        print(notes + '\n')

filenames = ['cat.txt','dog.txt']
for filename in filenames:
    cat_and_dog(filename)
