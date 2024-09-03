register = [ 'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'match', 'nonlocal',
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield' ]

accept = 'abcdefghijklmnopqrstuvwxyz0123456789_'

name = input("Введіть ім'я змінної: ")

if not name:
    print(False)
else:
    if name[0].isdigit():
        print(False)
    else:
        not_correct = False
        for char in name:
            if char not in accept or char.isupper():
                not_correct = True
                break
        if not_correct:
            print(False)
        else:
            if name.count('_') > 1:
                print(False)
            elif name in register:
                print(False)
            else:
                print(True)