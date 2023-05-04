from random import randint, choice
from datetime import datetime

print(datetime.now())

name = input("Enter your name: ")

"""while True:
    if len(name) in range(10):
        continue
    elif len(name) == 0:
        print("Name can't be blank. Enter your name again")
    elif len(name) >= 10:
        print("Max length for name is 10. Enter your name again")
    else:
        print("Wrong syntax. Enter your name again")"""

surname = input("Enter your surname: ")

"""while True:
    if len(name) in range(10):
        pass
    elif len(name) == 0:
        print("Name can't be blank. Enter name again")
    elif len(name) >= 10:
        print("Max length for name is 10. Enter name again")
    else:
        print("Wrong syntax. Enter name again")"""

a = len(name)
b = len(surname)
uniqueCodeList = []

alphabet = 'qwertyuiopasdfghjklzxcvbnm'


unique_code = choice(alphabet) + str(randint(1, 9)) + surname[0] + name[1] + '-' + \
              choice(surname) + str(a*b) + '-' + \
              surname[2::-2] + str(randint(10, 99))

uniqueCodeList.append(unique_code.upper())

print(unique_code.upper())
print(uniqueCodeList)
print(surname[2::-2])
