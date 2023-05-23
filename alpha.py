from random import randint, choice

def uno(surname, name):
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    return choice(alphabet) + str(randint(1, 9)) + surname[0] + name[1] + '-'