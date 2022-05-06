#####this will be a full converter between decimal, binary and hexidecimal####
###imports
import os, math

###functions 
def decimal_to_binary(number):
    
    ##setting variables
    number_list = []
    binary_list = []
    binary = ''

    ##defining logic 

    #making the list of numbers eg -> [10, 5, 2.5, 1.....]
    while number > 0.5:
        number = number / 2
        number_list.append(number)
        if number.is_integer() == False:
            number = math.floor(number)
    
    #converting integers to 0 and non integers to 1
    for number in number_list:
        if number.is_integer() == True:
            binary_list.append(0)
        else:
            binary_list.append(1)
    
    #concatinating all 1's and 0's together, importantly not adding them 
    for integer in reversed(binary_list):
        binary = str(binary) + str(integer)
    
    print(binary)


def binary_to_decimal(binary):
    
    ##setting variables
    reverse_list = []
    addition_list = []
    counter = 0
    total = 0

    ##defining logic
    #reversing the initial binary number 001 -> 100
    for bit in str(binary):
        reverse_list.append(bit)
    
    #filtering by 1's and adding 2 to the power of the counter (giving our index of were the 1 is)
    for bit in reversed(reverse_list):
        if bit == '1':
            addition_list.append(2**counter)
        counter = counter + 1
    
    #adding all the numbers together 
    for number in addition_list:
        total = int(number) + int(total)
    
    print(total)
        
###main event
while True:
    
    #taking the user input with formating 
    type_1 = str(input('Would you like to start with decimal (d) or binary (b): ')).lower()
    
    #defining which function to run
    if type_1 == 'd':
        integer = float(input('what is your number: '))
        decimal_to_binary(integer)
    elif type_1 == 'b':
        binary = int(input('what is your number: '))
        binary_to_decimal(binary)
    