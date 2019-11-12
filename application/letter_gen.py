import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
def random_letters():
    j = 0
    letters = []
    while j <= 3:
        i = random.randint(0,25)
        print(i)
        letters.append(alphabet[i])
        j+=1
    return(letters)