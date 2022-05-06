####types of variable and common functions####
###imports
import math

###variables
list_variable = ['a', 'b', 'c']
string_variable = 'hello'
integer_variable = 5

###functions
def list_functions(list_var):
    print(list_var)

    print(reversed(list_var))

    list_var.append('d')
    print(list_var)

    list_var.pop()
    print(list_var)

def string_functions(string_var):
    print(string_var)

    print(string_var.split('l'))

    string_var = string_var + ' world!'
    print(string_var)

    print(string_var[:4])

def integer_functions(integer_var):
    print(integer_var)

    integer_var = integer_var + integer_var
    print(integer_var)

    integer_var = integer_var * 2
    print(integer_var)

    integer_var = integer_var / 2
    print(integer_var)

    integer_var = integer_var ** 2
    print(integer_var)

###main event
while True:
    #list_functions(list_variable)
    #string_functions(string_variable)
    integer_functions(integer_variable)
    break