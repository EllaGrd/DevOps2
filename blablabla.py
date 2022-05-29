import requests
def save_name():
    n = input("enter your name: ")
    my_file = open("names.txt", "a")
    my_file.write(f"{n}\n")


def show_names():
    with open("names.txt") as moshe:
        for line in moshe.readlines():
            print(f"hello {line}", end='')

def url_caller(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"{url} is ok")

def call_urls():
    with open("urls.txt") as urls:
        for line in urls.readlines():
            url_caller(line.strip())

# save_name()
call_urls()

try:
    a = int(input("enter first number: "))
    b = int(input("enter second number: "))
    print(a / b)
    r = open("file_not_exists.txt")
except ZeroDivisionError:
    print("could not divide by zero")
except FileNotFoundError:
    print("could not find file")
except Exception as e:
    print(e.args)
print("blablabalbla")

# https://docs.python.org/3/library/exceptions.html#concrete-exceptions

from datetime import datetime
def my_decorator(func):
    def wrapper():
        print(datetime.now())
        func()
        print(datetime.now())
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

@my_decorator
def say_bark():
    print("whoof!")

say_whee()
say_bark()