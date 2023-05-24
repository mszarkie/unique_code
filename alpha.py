from random import randint, choice


def uno(surname, name):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    return choice(alphabet) + str(randint(1, 9)) + surname[0] + name[1] + '-'


def dos(surname, name):
    a = len(name)
    b = len(surname)
    return choice(surname) + str(a*b) + '-'


def tres(surname):
    return surname[2::-2] + str(randint(10, 99))
