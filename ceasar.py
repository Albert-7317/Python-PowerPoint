####ceasar cipher####
import random

#variables

shift = random.randint(0, 100)
game_state = True

#functions
def encode(string, shift):
    message = ''
    message_list = []

    for charecter in string:
        init_int_charecter = ord(charecter)
        int_charecter = init_int_charecter + shift
        message_list.append(str(int_charecter))
    
    for integer in message_list:
        charecter = str(integer)
        message = message + charecter + str(shift)

    with open('other_secret_message.txt', 'w') as f:
        f.write(message)


#main event
while game_state:
    secret_message = input('what is your secret message: ')
    encode(secret_message, shift)
    break