def getnum():
    return int(input("Enter number"))

def sumdigits(number):
    sum=0

    while number > 0:
        sum += number % 10

        number = number//10
    return sum

print(sumdigits(getnum()))