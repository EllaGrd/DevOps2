isTrue = False
a = 2
b = 2
strOne = "One"
strThree = "Three"
c = [1, 2, 3]
d = [1, 2, 3]
if type(a) is int:
    print("a equels b")
if c == d:
    print("c equels d")
if a is b:
    print("a is b")
if c is d:
    print("c is d")

age = int(input("enter your age: "))
if 0 < age < 120:
    print("ok")
my_names = ["adi", "ben", "noam", "arthur", "ron"]
my_list = []
if my_list:
    print("my_list is not empty")
if my_names:
    print("my_names is not empty")
    if len(my_names) > 2:
        print("i remember enough names")
        print(len(my_names))

if "zohar" not in my_names:
    print("found it zoar")

### if my_names[0] == ["zoar"]
    print("found it zoar")
if a < b and strThree == 3 or isTrue == 4:
    print("a is less than b")
elif a == b:
    print("a is equel b")
elif strOne != strThree:
    print("hello")
else:
    print("a is greater than b")
