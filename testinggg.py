from random import randint, choice
from datetime import datetime
from alpha import uno

actual_date = datetime.now()
seconds = actual_date.strftime('%S')
micro_seconds = actual_date.strftime('%f')


# print(seconds[-1])
#
# print(micro_seconds[0::4])


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

two_letters = choice(alphabet) + choice(alphabet)
print("this is choice x2:", two_letters)

<<<<<<< HEAD# alpha = choice(alphabet) + str(randint(1, 9)) + surname[0] + name[1] + '-'
beta = choice(surname) + str(a*b) + '-'
omega = surname[2::-2] + str(randint(10, 99))


unique_code = uno(surname, name) + beta + omega

alpha = choice(alphabet) + str(randint(1, 9)) + surname[0] + name[1] + '-'
beta = choice(surname) + str(a*b) + '-'
omega = surname[2::-2] + str(randint(10, 99))

unique_code = alpha + beta + omega


uniqueCodeList.append(unique_code.upper())

print(unique_code.upper())
print(uniqueCodeList)
print(surname[2::-2])
