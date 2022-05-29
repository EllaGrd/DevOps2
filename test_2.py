string = ''
for i in range(int(input("Enter Number: "))):
    string += '#'
    print(string)

for i in range (1,8):
    string = ''
    for j in range(1,8):
       if j==i or j==(8-i):
          string += '#'
       else:
          string += ' '
    print(string)

def getnum():
    return int(input("Enter number"))

def sumdigits(number):
    sum=0

    while number > 0:
        sum += number % 10

        number = number//10
    return sum

print(sumdigits(getnum()))