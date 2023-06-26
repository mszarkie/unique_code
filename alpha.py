from random import randint, choice, shuffle
from datetime import datetime


def uno():
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    str_to_list = " ".join(alphabet).split()
    shuffle(str_to_list)
    x = str_to_list[2::-2]
    list_to_str = ''.join([str(elem) for elem in x])
    return list_to_str + str(randint(10, 99)) + '-'


def dos():
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    actual_date = datetime.now()
    seconds = actual_date.strftime('%S')
    return choice(alphabet) + str(randint(1, 9)) + choice(alphabet) + seconds[-1] + '-'


def tres():
    actual_date = datetime.now()
    micro_seconds = actual_date.strftime('%f')
    xyz = 'xyz'
    return micro_seconds[0::4] + choice(xyz) + micro_seconds[-1] + '-'


def quatro():
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    xyz = 'xyz'
    return str(randint(0, 9)) + choice(alphabet) + choice(xyz) + str(randint(0, 9))


