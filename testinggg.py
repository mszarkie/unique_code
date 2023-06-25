from random import choice
from datetime import datetime
from alpha import uno, dos, tres, quatro

name = input("Enter your name: ")
surname = input("Enter your surname: ")

"""while True:
    if len(name) in range(10):
        continue
    elif len(name) == 0:
        print("Name can't be blank. Enter your name again")
    elif len(name) >= 10:
        print("Max length for name is 10. Enter your name again")
    else:
        print("Wrong syntax. Enter your name again")"""

# if len(str(value)) != 13:
#     ValidationError('ISBN must contains 13 digits')
# o tak o sie to robi


"""while True:
    if len(name) in range(10):
        pass
    elif len(name) == 0:
        print("Name can't be blank. Enter name again")
    elif len(name) >= 10:
        print("Max length for name is 10. Enter name again")
    else:
        print("Wrong syntax. Enter name again")"""

actual_date = datetime.now()
seconds = actual_date.strftime('%S')
micro_seconds = actual_date.strftime('%f')


print("seconds", seconds[-1])
#
print("micros:", micro_seconds[0::4])

uniqueCodeList = []

alphabet = 'qwertyuiopasdfghjklzxcvbnm'

two_letters = choice(alphabet) + choice(alphabet)
print("this is choice x2:", two_letters)

a = uno(surname, name)
b = dos(surname, name)
c = tres(surname)
d = quatro()

unique_code = a + b + c + d

uniqueCodeList.append(unique_code.upper())

print(unique_code.upper())
print(uniqueCodeList)
print(surname[2::-2])
