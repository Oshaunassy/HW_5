import random
from random import randint, choice

def numbers():
    return random.randint(1, 31)

def lucky(win_slot, bet):
    return bet == win_slot


# slot = list(range(1, 31))
# win_slot = random.choice(slot)
# bet = int(input('Сделайте ставку: '))
