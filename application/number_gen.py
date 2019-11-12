import random

def random_numbers():
    j = 0
    numbers = []
    while j <= 3:
        i = random.randint(0,9)
        numbers.append(str(i))
        j += 1
    return(numbers)
        
