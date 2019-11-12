import random

choices = 'abcdefghijklmnopqrstuvwxyz0123456789'
def ref_gen():
    ref_list = []
    while len(ref_list)<=12:
        num = random.randint(0,35)
        ref_list.append(str(choices[num]))
    ref = ''.join(ref_list)
    return ref
    
print(ref_gen())