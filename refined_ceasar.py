####ceacar cipher####
import random

#function
def encode(string):
    shift = random.randint(0, 100)
    message = ''
    with open('secret_message.txt', 'w') as f:
        for charecter in string:
            message = message + str((ord(charecter) + shift)) + str(shift)
        f.write(message)

#event
while True:
    secret_message = str(input('what is your secret message: '))
    encode(secret_message)
    break
