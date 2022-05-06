####NAME AND PURPOSE OF PROGRAMME####
###IMPORTS###
import random

###VARIABLES###
random = random.randint(0, 10)

###FUNCTIONS###
def random_loop(number):
    for i in range(0, number):
        print(i)

###MAIN EVENT###
while True:
    random_loop(random)
    break