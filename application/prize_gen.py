import random

def random_prize():
    prize_number = random.randint(0,100)
    if prize_number == 100:
        prize = 1000000
    elif prize_number >= 98:
        prize = 500000
    elif prize_number >= 93:
        prize = 250000
    elif prize_number >= 86:
        prize = 100000
    elif prize_number >= 76:
        prize = 50000
    elif prize_number >= 61:
        prize = 10000
    elif prize_number >= 41:
        prize = 5000
    elif prize_number >= 16:
        prize = 1000
    else:
        prize = 1
    return(prize)
