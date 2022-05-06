import os, math
def decimal_to_binary(number):
    Memorable_name = []
    something_funny = []
    OverlyExplainName = ''
    while number > 0.5:
        number = number / 2
        Memorable_name.append(number)
        if number.is_integer() == False:
            number = math.floor(number)
    for number in Memorable_name:
        if number.is_integer() == True:
            something_funny.append(0)
        else:
            something_funny.append(1)
    for integer in reversed(something_funny):
        OverlyExplainName = str(OverlyExplainName) + str(integer)
    print(OverlyExplainName)
game_state = True
def converter2(binary):
    Reverseing = []
    sensibleName = []
    some_numberThing = 0
    total = 0  
    for bit in str(binary):
        Reverseing.append(bit)    
    for bit in reversed(Reverseing):
        if bit == '1':
            sensibleName.append(2**some_numberThing)
        some_numberThing = some_numberThing + 1
    for number in sensibleName:
        total = int(number) + int(total)    
    print(total)
while game_state:   
    type_1 = str(input('Would you like to start with decimal (d) or binary (b): '))
    if type_1 == 'd':
        integer = float(input('what is your number: '))
        decimal_to_binary(integer)
    elif type_1 == 'b':
        binary = int(input('what is your number: '))
        converter2(binary)
        