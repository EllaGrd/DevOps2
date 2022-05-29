


def square(num):
    result = num * num
    return result, num

a = square(16)
print(a)
square(10)

a = int(input("enter your age: "))
if 0 < a < 120:
    print("ok")
else:
    print("not ok")
b = int(input("enter amount of pets: "))
if 0 < b < 4:
    print("ok")
else:
    print("not ok")


def validate(prompt):
    a = int(input(prompt))
    if 0 < a < 120:
        print("ok")
    else:
        print("not ok")


validate("enter your age:")


def validate(prompt, low, high):
    global a    # not use global please !!!
    a = int(input(prompt))
    if 0 < a < 120:
        print("ok")
    else:
        print("not ok")


validate("enter your age:", 0, 120)


def validate(prompt, low, high, ok, not_ok):
    a = int(input(prompt))
    if low < a < high:
        print("ok")
    else:
        print("not ok")