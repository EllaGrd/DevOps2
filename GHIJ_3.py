my_file = open("c:/Users/BWX367/PycharmProjects/DevOps2/words.txt",'w+')
my_file.write("Ella")
my_file.close()

my_file = open("c:/Users/BWX367/PycharmProjects/DevOps2/words.txt",'r')
content = my_file.read()
print(content)
my_file.close()

my_file1 = open("c:/Users/BWX367/PycharmProjects/DevOps2/hebrew.txt",'w+',encoding='utf-8')
my_file1.write("דגכיעק'ט'אר")
my_file1.close()

my_file1 = open("c:/Users/BWX367/PycharmProjects/DevOps2/hebrew.txt",'r',encoding='utf-8')
content = my_file1.read()
print(content)
my_file1.close()

# OR

my_file2 = open("c:/Users/BWX367/PycharmProjects/DevOps2/Daniel.txt",'w+',encoding='utf-8')
my_file2.write("Daniel \n")
my_file2.write("שלום")
my_file2 = open("c:/Users/BWX367/PycharmProjects/DevOps2/Daniel.txt",'r',encoding='utf-8')
str = my_file2.read()
print(str)
my_file2.close()


