'''
Virutal Coin Toss 

Instructions
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

'''

import random

test_seed = int(input("Create a seed number:"))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
    print('Heads')
else: 
    print('Tails')