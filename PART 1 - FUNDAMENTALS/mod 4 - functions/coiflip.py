import random

for i in range(100): # 100 coin flips
    if random.randint(0,1) == 0:
        print('H', end=' ')
    else: 
        print('T', end=' ')
print() #print one newline(?) at the end