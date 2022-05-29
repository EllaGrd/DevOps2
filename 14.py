try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a / b)
    r = open("file_not_exists.txt")
except Exception as e:
 print("something went wrong")
 print("blablabla")
except ZeroDivisionError:
    print("could not divide by zero")
except FileNotFoundError:
    print("could not found ERROR")

import requests
requests.get("http://www.google.com")
