from sys import  argv , exit

def contains_only_y_in_x(x , y):
    value = False
    for i in x:
        if y in i or not i:
            value = False
        else:
            value = True
            break
    return value


if len(argv) < 2:
    exit('Too few command-line arguments')
if len(argv) > 2:
    exit('Too many command-line arguments')
if len(argv) == 2 and not (argv[1].endswith('.py')):
    exit('Not a Python file')
else:
    try:
        file = open(argv[1] , 'r')
    except FileNotFoundError:
        exit('File does not exist')
    else:
        lines = file.readlines()
        num_of_lines_true = 0
        for line in lines:
            if not(line.startswith('#')) or contains_only_y_in_x(line , ' '):
                num_of_lines_true += 1
        print(num_of_lines_true)
