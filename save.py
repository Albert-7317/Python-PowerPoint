###variables
code_snippet = str('this is some really cool code!')

###function
def save(string):
    with open('save.txt', 'w') as f:
        f.write(string)

###main event
while True:
    save(code_snippet)
    break