a = "hello world"
print(a)
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print("hello world")
print(list(range(5)))
print(list(range(1, 5)))
print(list(range(20, -10, -3)))

for i in range(5):
    print(f"{i} hello")
    print(f"hello world")
    my_names = ["adi", "ben", "noam", "arthur"]
    print(f"hello world #{i}")

for name in my_names:
    print(f"hello {name}")
    if name == "arthur":
        break
else:
    print("printed all names")


for i in range(len(my_names)):
    print(my_names[i])

for i in range(len(my_names)):
    my_names[i] = "moshe"
    print(my_names[i])

a = 0
while a < 5:
    print(a)
    a = a + 1

a = 0
while a < 5:
    print(a)
    a = a + 1
    if a == 2:
        continue
    print("after continue")

l = []
current_input = input("enter letter: ")
while current_input != "q":
    l.append(current_input)
    current_input = input("enter letter: ")
print(f"inputs are {l}")

n = [1, 2, 3, 4, 5]
result = [num * 2 for num in n if num > 2]
for num in n:
    if num > 2:
        result.append(num * 2)






