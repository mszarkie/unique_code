from random import randint, choice
from datetime import datetime


def uno(surname, name):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    return choice(alphabet) + str(randint(1, 9)) + surname[0] + name[2] + '-'


def dos(surname, name):
    a = len(name)
    b = len(surname)
    actual_date = datetime.now()
    seconds = actual_date.strftime('%S')
    return choice(surname) + str(a*b) + seconds[-1] + '-'


def tres(surname):
    return surname[2::-2] + str(randint(10, 99))
