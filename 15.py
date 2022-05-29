def get_age():
    age = int(input("enter your age: "))
    if age < 0:
        raise ValueError("age can not be negative")

try:
    get_age()
except ValueError as e:
    print(e.args)
print("blablabalbla")

  a = input("enter number: ")
def check_my_number(num):
  a = 0
try:
    a = (num)
except ValueError:
    return False






